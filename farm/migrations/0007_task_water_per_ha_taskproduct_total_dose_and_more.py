# Generated by Django 5.0.11 on 2025-03-10 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0006_alter_task_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='water_per_ha',
            field=models.FloatField(default=1000, help_text='Litros de agua por hectárea'),
        ),
        migrations.AddField(
            model_name='taskproduct',
            name='total_dose',
            field=models.FloatField(blank=True, help_text='Dosis total calculada', null=True),
        ),
        migrations.AddField(
            model_name='taskproduct',
            name='total_dose_unit',
            field=models.CharField(blank=True, choices=[('L', 'Litros'), ('kg', 'Kilogramos')], max_length=10, null=True),
        ),
    ]
