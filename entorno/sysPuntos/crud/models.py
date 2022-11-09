from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class direccion(models.Model):
    nombre = models.CharField(max_length = 50)
    descripcion = models.TextField()
    
    def __str__(self):
        return self.nombre
    
class cliente(models.Model):
    rut_cliente = models.CharField(unique=True, max_length = 10, primary_key=True)
    username = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank = True )
    direccion = models.ForeignKey(direccion, on_delete = models.CASCADE, null = True, blank = True )
    nombre = models.CharField(max_length = 30)
    apellido_pa = models.CharField(max_length = 30)
    apellido_ma = models.CharField(max_length = 30)
    
    def __str__(self):
        return self.rut_cliente