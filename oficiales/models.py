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

class Oficial(models.Model):
    id_carnet = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    cedula = models.CharField(max_length=13)
    estado = models.CharField(max_length=20, choices=ESTADOS)
    ubicacion = models.CharField(max_length=100)
    zona = models.CharField(max_length=100)
    tipo = models.CharField(max_length=10, choices=[('Fijo', 'Fijo'), ('Cubridor', 'Cubridor')])
    turno = models.CharField(max_length=10, choices=[('Día', 'Día'), ('Noche', 'Noche')])
    fecha_ingreso = models.DateField(default=date.today)
    tipo_oficial = models.CharField(max_length=20, choices=TIPOS)
    archivo_adjunto = models.FileField(upload_to='archivos_oficiales/', blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} ({self.id_carnet})"
