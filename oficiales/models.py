from django.db import models
from datetime import date

ESTADOS = [
    ('Activo', 'Activo'),
    ('Suspendido', 'Suspendido'),
    ('Ausente', 'Ausente'),
    ('Licencia', 'Licencia'),
]

TIPOS = [
    ('Regular', 'Regular'),
    ('Jefe de Grupo', 'Jefe de Grupo'),
    ('VIP', 'VIP'),
    ('Supervisor', 'Supervisor'),
    ('Motorizado', 'Motorizado'),
    ('Otro', 'Otro'),
]

TIPO_CHOICES = [('Fijo', 'Fijo'), ('Cubridor', 'Cubridor')]
TURNO_CHOICES = [('Día', 'Día'), ('Noche', 'Noche')]

class Vehiculo(models.Model):
    placa = models.CharField(max_length=20, unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.placa

class Oficial(models.Model):
    id_carnet = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    cedula = models.CharField(max_length=13)
    estado = models.CharField(max_length=20, choices=ESTADOS)
    ubicacion = models.CharField(max_length=100)
    zona = models.CharField(max_length=100)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    turno = models.CharField(max_length=10, choices=TURNO_CHOICES)
    fecha_ingreso = models.DateField(default=date.today)
    tipo_oficial = models.CharField(max_length=20, choices=TIPOS)
    archivo_adjunto = models.FileField(upload_to='archivos_oficiales/', blank=True, null=True)
    dias_libres_tomados = models.IntegerField(default=0)
    dias_libres_trabajados = models.IntegerField(default=0)
    dias_cubiertos = models.IntegerField(default=0)
    dias_regulares = models.IntegerField(default=26)
    vehiculo_asignado = models.ForeignKey(
        Vehiculo,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='supervisores_asignados'
    )

    def es_supervisor(self):
        return self.tipo_oficial == 'Supervisor'

    def __str__(self):
        return f"{self.nombre} ({self.id_carnet})"
