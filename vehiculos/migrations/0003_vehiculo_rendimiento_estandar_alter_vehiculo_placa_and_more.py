# Generated by Django 5.2 on 2025-04-22 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0002_vehiculo_activo_vehiculo_asignado_a_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiculo',
            name='rendimiento_estandar',
            field=models.FloatField(default=0.0, help_text='Km por galón'),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='placa',
            field=models.CharField(max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='tipo',
            field=models.CharField(choices=[('Carro', 'Carro'), ('Camioneta', 'Camioneta'), ('Motor', 'Motor'), ('SUV', 'SUV'), ('Camión', 'Camión'), ('Otro', 'Otro')], max_length=30),
        ),
    ]
