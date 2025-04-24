from django import forms
from .models import CargaCombustible

class CargaCombustibleForm(forms.ModelForm):
    class Meta:
        model = CargaCombustible
        fields = [
            'fecha',
            'vehiculo',
            'supervisor',
            'km_inicial',
            'km_final',
            'galones',
            'precio_por_galon',
            'archivo_gps',
            'archivo_reporte',
        ]
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'vehiculo': forms.Select(attrs={'class': 'form-select'}),
            'supervisor': forms.TextInput(attrs={'class': 'form-control'}),
            'km_inicial': forms.NumberInput(attrs={'class': 'form-control'}),
            'km_final': forms.NumberInput(attrs={'class': 'form-control'}),
            'galones': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'precio_por_galon': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'archivo_gps': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'archivo_reporte': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        km_inicial = cleaned_data.get('km_inicial')
        km_final = cleaned_data.get('km_final')
        galones = cleaned_data.get('galones')

        if km_inicial is not None and km_final is not None and km_final <= km_inicial:
            self.add_error('km_final', "El kilometraje final debe ser mayor que el inicial.")

        if galones is not None and galones <= 0:
            self.add_error('galones', "Los galones deben ser mayores que cero.")

        return cleaned_data





