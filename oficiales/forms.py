from django import forms
from .models import Oficial

class OficialForm(forms.ModelForm):
    class Meta:
        model = Oficial
        fields = '__all__'
        widgets = {
            'fecha_ingreso': forms.DateInput(attrs={'type': 'date'}),
        }
