

from django import forms
from .models import Arma
from django.contrib.auth import authenticate


class ArmaForm(forms.ModelForm):
    class Meta:
        model = Arma
        fields = ['codigo', 'serie', 'tipo', 'marca', 'calibre', 'licencia', 'licencia_digital', 'estado', 'observaciones']
        widgets = {
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'serie': forms.TextInput(attrs={'class': 'form-control'}),
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'calibre': forms.TextInput(attrs={'class': 'form-control'}),
            'licencia': forms.TextInput(attrs={'class': 'form-control'}),
            'licencia_digital': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }



class ConfirmarPasswordForm(forms.Form):
    password = forms.CharField(
        label="Contraseña del administrador",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Ingrese su contraseña"})
    )

    def __init__(self, *args, **kwargs):
        self.usuario = kwargs.pop("usuario", None)
        super().__init__(*args, **kwargs)

    def clean_password(self):
        password = self.cleaned_data.get("password")
        if not self.usuario.check_password(password):
            raise forms.ValidationError("La contraseña no es correcta.")
        return password



class PasswordForm(forms.Form):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Contraseña de administrador"
    )
