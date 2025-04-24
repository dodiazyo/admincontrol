from django.db import models

ESTADO_ARMAS = [
    ('Disponible', 'Disponible'),
    ('Asignada', 'Asignada'),
    ('Mantenimiento', 'Mantenimiento'),
    ('Baja', 'Baja'),
]

TIPO_ARMAS = [
    ('Pistola', 'Pistola'),
    ('Pistola Eléctrica', 'Pistola Eléctrica'),
    ('Escopeta', 'Escopeta'),
    ('Revólver', 'Revólver'),
    ('Rifle', 'Rifle'),
    ('Subfusil', 'Subfusil'),
    ('Carabina', 'Carabina'),
    ('Fusil de Asalto', 'Fusil de Asalto'),
    ('Otro', 'Otro'),
]

class Arma(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    serie = models.CharField(max_length=50, unique=True)
    tipo = models.CharField(max_length=50, choices=TIPO_ARMAS)
    marca = models.CharField(max_length=50, default='Desconocida')
    calibre = models.CharField(max_length=20, blank=True, null=True)
    licencia = models.CharField(max_length=100, blank=True, null=True)
    licencia_digital = models.FileField(upload_to='licencias_armas/', blank=True, null=True)
    estado = models.CharField(max_length=20, choices=ESTADO_ARMAS, default='Disponible')
    fecha_ingreso = models.DateField(auto_now_add=True)
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.codigo} - {self.serie}"


class Inventario(models.Model):
    arma = models.OneToOneField(Arma, on_delete=models.CASCADE)
    fecha_ingreso = models.DateField(auto_now_add=True)
    ubicacion = models.CharField(max_length=100, default="Almacén principal")

    def __str__(self):
        return f"Inventario - {self.arma.codigo}"
