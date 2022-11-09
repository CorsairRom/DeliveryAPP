from django import forms
from .models import cliente



class ClienteForm(forms.ModelForm):
    
    class Meta:
        model = cliente
        field = ["nombre", "apellido_pa", "apellido_ma", "rut_cliente", "direccion"]
        exclude = ("username",)