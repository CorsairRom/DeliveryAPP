from dataclasses import field
from django import forms
from .models import cliente, direccion
from django.contrib.auth.forms import UserCreationForm


class ClienteForm(forms.ModelForm):
    
    class Meta:
        model = cliente
        field = ["nombre", "apellido_pa", "apellido_ma", "rut_cliente", "direccion"]
        exclude = ("username",)

class Custom (UserCreationForm):
    pass

class DireccionesForm(forms.ModelForm):
    
    class Meta:
        model = direccion
        field = ["nombre_dir", "descripcion"]
        exclude = ("cliente_dir",)