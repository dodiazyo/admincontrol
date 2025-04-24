from django.db import models
from vehiculos.models import Vehiculo  # Asegúrate de que el modelo Vehiculo exista

class CargaCombustible(models.Model):
    fecha = models.DateField()
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    supervisor = models.CharField(max_length=100)
    km_inicial = models.PositiveIntegerField()
    km_final = models.PositiveIntegerField()
    galones = models.DecimalField(max_digits=5, decimal_places=2)
    precio_por_galon = models.DecimalField(max_digits=6, decimal_places=2)
    archivo_gps = models.FileField(upload_to='gps/', blank=True, null=True)
    archivo_reporte = models.FileField(upload_to='reportes_combustible/', blank=True, null=True)

    def recorrido(self):
        return self.km_final - self.km_inicial

    def rendimiento(self):
        try:
            return self.recorrido() / float(self.galones)
        except ZeroDivisionError:
            return 0

    def total_pago(self):
        return self.galones * self.precio_por_galon

    def km_esperado(self, rendimiento_teorico=7.97):
        return self.galones * rendimiento_teorico

    def sobrepaso_km(self):
        return self.recorrido() > self.km_esperado()

    def __str__(self):
        return f"{self.vehiculo} - {self.fecha}"
