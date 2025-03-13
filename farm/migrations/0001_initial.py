# Generated by Django 5.0.11 on 2025-02-24 21:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('area', models.FloatField()),
                ('crop', models.CharField(max_length=100)),
                ('planting_year', models.IntegerField()),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=50)),
                ('capacity', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('fertilizer', 'Fertilizante'), ('pesticide', 'Fitosanitario')], max_length=50)),
                ('dose', models.FloatField()),
                ('dose_type', models.CharField(choices=[('kg_per_2000l', 'kg/2000L agua'), ('kg_per_1000l', 'kg/1000L agua'), ('l_per_2000l', 'L/2000L agua'), ('l_per_1000l', 'L/1000L agua'), ('kg_per_ha', 'kg/ha'), ('l_per_ha', 'L/ha')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Harvest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('amount', models.FloatField()),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farm.field')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('spraying', 'Pulverización'), ('fertigation', 'Fertirrigación')], max_length=20)),
                ('date', models.DateField()),
                ('status', models.CharField(choices=[('pending', 'Pendiente'), ('completed', 'Completada'), ('delayed', 'Retrasada')], max_length=20)),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farm.field')),
                ('machine', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='farm.machine')),
            ],
        ),
        migrations.CreateModel(
            name='TaskProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dose', models.FloatField()),
                ('dose_type', models.CharField(choices=[('kg_per_2000l', 'kg/2000L agua'), ('kg_per_1000l', 'kg/1000L agua'), ('l_per_2000l', 'L/2000L agua'), ('l_per_1000l', 'L/1000L agua'), ('kg_per_ha', 'kg/ha'), ('l_per_ha', 'L/ha')], max_length=20)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farm.product')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farm.task')),
            ],
            options={
                'unique_together': {('task', 'product')},
            },
        ),
        migrations.AddField(
            model_name='task',
            name='products',
            field=models.ManyToManyField(through='farm.TaskProduct', to='farm.product'),
        ),
    ]
