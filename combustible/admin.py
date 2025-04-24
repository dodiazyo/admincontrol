from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import CargaCombustible

@admin.register(CargaCombustible)
class CargaCombustibleAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'vehiculo', 'supervisor', 'recorrido', 'rendimiento', 'total_pago')
    list_filter = ('vehiculo', 'fecha')
    search_fields = ('supervisor',)
