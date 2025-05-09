# Generated by Django 5.2 on 2025-04-22 02:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('armas', '0002_arma_fecha_ingreso_arma_licencia_arma_marca_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_ingreso', models.DateField(auto_now_add=True)),
                ('ubicacion', models.CharField(default='Almacén principal', max_length=100)),
                ('arma', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='armas.arma')),
            ],
        ),
    ]
