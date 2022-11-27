from dataclasses import field
from django import forms
from .models import cliente
from django.contrib.auth.forms import UserCreationForm


class ClienteForm(forms.ModelForm):
    
    class Meta:
        model = cliente
        field = ["nombre", "apellido_pa", "apellido_ma", "rut_cliente", "direccion"]
        exclude = ("username",)

class Custom (UserCreationForm):
    pass