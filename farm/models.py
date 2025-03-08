from datetime import datetime

from django.db import models


class Field(models.Model):
    name = models.CharField(max_length=100)
    area = models.FloatField()  # en hectáreas o m²
    crop = models.CharField(max_length=100)
    planting_year = models.IntegerField()
    location = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class Machine(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)  # Ej. Pulverizador
    capacity = models.FloatField()  # Capacidad en litros


class Product(models.Model):
    DOSE_TYPE_CHOICES = [
        ('kg_per_2000l', 'kg/2000L agua'),
        ('kg_per_1000l', 'kg/1000L agua'),
        ('l_per_2000l', 'L/2000L agua'),
        ('l_per_1000l', 'L/1000L agua'),
        ('kg_per_ha', 'kg/ha'),
        ('l_per_ha', 'L/ha'),
    ]
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50, choices=[('fertilizer', 'Fertilizante'), ('pesticide', 'Fitosanitario')])
    dose = models.FloatField()  # Dosis del producto
    dose_type = models.CharField(max_length=20, choices=DOSE_TYPE_CHOICES)

    def __str__(self):
        return self.name


class Task(models.Model):
    TYPE_CHOICES = [
        ('spraying', 'Pulverización'),
        ('fertigation', 'Fertirrigación'),
        ('pest_control', 'Fumigación'),
        ('nutrition', 'Nutrición'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pendiente'),
        ('completed', 'Completada'),
        ('delayed', 'Retrasada'),
    ]

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    creation_timestamp = models.DateTimeField(auto_now_add=True)
    update_timestamp = models.DateTimeField(auto_now=True)
    date = models.DateField()
    finish_date = models.DateField(null=True, blank=True)
    field = models.ForeignKey('farm.Field', on_delete=models.CASCADE)
    machine = models.ForeignKey('farm.Machine', on_delete=models.SET_NULL, null=True, blank=True)
    products = models.ManyToManyField('farm.Product', through='TaskProduct')

    def __str__(self):
        return f"{self.name} - {self.date}"

    def is_pending(self):
        return not self.finish_date and self.date >= datetime.now().date()

    def is_completed(self):
        return self.finish_date is not None

    def is_delayed(self):
        return not self.finish_date and self.date < datetime.now().date()

    def status(self):
        if self.is_completed():
            return 'completed'
        elif self.is_delayed():
            return 'delayed'
        else:
            return 'pending'

    # métodos para mostrar en el template
    def status_display(self):
        # Devuelve el valor legible para el template
        status_map = {
            'pending': 'Pendiente',
            'completed': 'Completada',
            'delayed': 'Retrasada',
        }
        return status_map.get(self.status(), 'Desconocido')

    def state_class(self):
        status_map = {
            'pending': 'warning',
            'completed': 'success',
            'delayed': 'danger',
        }
        return status_map.get(self.status(), 'secondary')  # 'secondary' como fallback

    def type_class(self):
        type_map = {
            'spraying': 'spray-can-sparkles',
            'fertigation': 'droplet',
            'pest_control': 'bug',
            'nutrition': 'leaf',
        }
        return type_map.get(self.type, 'secondary')  # 'secondary' como fallback


class TaskProduct(models.Model):
    task = models.ForeignKey("Task", on_delete=models.CASCADE)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    dose = models.FloatField()
    dose_type = models.CharField(max_length=20, choices=Product.DOSE_TYPE_CHOICES)  # Agregar esto

    class Meta:
        unique_together = ('task', 'product')  # Evita duplicados

    def __str__(self):
        return f"{self.product.name} en {self.task} - {self.dose}"


class Harvest(models.Model):
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.FloatField()  # kg o toneladas
