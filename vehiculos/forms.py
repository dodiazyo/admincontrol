# vehiculos/forms.py
from django import forms
from .models import Vehiculo, ChequeoDiario

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = '__all__'
        widgets = {
            'fecha_mantenimiento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'fecha_ingreso': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

class ChequeoDiarioForm(forms.ModelForm):
    class Meta:
        model = ChequeoDiario
        fields = '__all__'
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
