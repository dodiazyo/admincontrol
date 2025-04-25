from django import forms
from .models import Oficial

class OficialForm(forms.ModelForm):
    class Meta:
        model = Oficial
        fields = [
            'id_carnet', 'nombre', 'cedula', 'estado', 'ubicacion', 'zona',
            'tipo', 'turno', 'fecha_ingreso', 'tipo_oficial', 'archivo_adjunto',
            'dias_libres_tomados', 'dias_libres_trabajados', 'dias_cubiertos',
            'dias_regulares', 'vehiculo_asignado',
        ]
        widgets = {
            'fecha_ingreso': forms.DateInput(attrs={'type': 'date'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
            'tipo_oficial': forms.Select(attrs={'class': 'form-select'}),
        }
