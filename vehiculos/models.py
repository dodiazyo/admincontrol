from django.db import models

TIPOS_VEHICULO = [
    ('Carro', 'Carro'),
    ('Motor', 'Motor'),
    ('Camioneta', 'Camioneta'),
    ('SUV', 'SUV'),
    ('Camión', 'Camión'),
    ('Otro', 'Otro'),
]

class Vehiculo(models.Model):
    tipo = models.CharField(max_length=30, choices=TIPOS_VEHICULO)
    placa = models.CharField(max_length=15, unique=True)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    año = models.PositiveIntegerField()
    rendimiento_estandar = models.FloatField(help_text="Km por galón", default=0.0)
    asignado_a = models.CharField(max_length=100, blank=True, null=True)
    kilometraje_actual = models.PositiveIntegerField(default=0)
    fecha_mantenimiento = models.DateField(blank=True, null=True)
    documento_seguro = models.FileField(upload_to='documentos_vehiculos/', blank=True, null=True)
    documento_matricula = models.FileField(upload_to='documentos_vehiculos/', blank=True, null=True)
    licencia_operacion = models.FileField(upload_to='documentos_vehiculos/', blank=True, null=True)
    fecha_ingreso = models.DateField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.tipo} - {self.placa}"

    def icono_tipo(self):
        return {
            'Carro': '🚗',
            'Motor': '🏍️',
            'Camioneta': '🚚',
            'SUV': '🚙',
            'Camión': '🚛',
            'Otro': '🚘'
        }.get(self.tipo, '🚘')

    def tipo_con_icono(self):
        iconos = {
            'Carro': '🚗',
            'Motor': '🏍️',
            'Camioneta': '🚚',
            'SUV': '🚙',
            'Camión': '🚛',
            'Otro': '🚘'
        }
        return f"{iconos.get(self.tipo, '🚘')} {self.tipo}"

class ChequeoDiario(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    supervisor = models.CharField(max_length=100)
    kilometraje = models.PositiveIntegerField()
    observaciones = models.TextField(blank=True, null=True)
    foto = models.ImageField(upload_to='chequeos_vehiculos/', blank=True, null=True)

    def __str__(self):
        return f"Chequeo {self.vehiculo.placa} - {self.fecha}"
