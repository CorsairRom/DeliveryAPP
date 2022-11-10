from django.db import models
from django.contrib.auth.models import User

# Create your models here.
 
class cliente(models.Model):
    rut_cliente = models.CharField(unique=True, max_length = 10, primary_key=True)
    username = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank = True )
    direccion_cli = models.CharField( max_length = 50)
    nombre = models.CharField(max_length = 30)
    apellido_pa = models.CharField(max_length = 30)
    apellido_ma = models.CharField(max_length = 30)
    
    def __str__(self):
        return self.rut_cliente
    
class direccion(models.Model):
    nombre_dir = models.CharField(max_length = 50)
    descripcion = models.TextField()
    cliente_dir = models.ForeignKey(cliente, on_delete = models.CASCADE, null = True, blank = True)
    def __str__(self):
        return self.nombre_dir
    
class usuarioPrueba(models.Model):
    rut = models.CharField(max_length = 50)
    id_tipo_usuario = models.IntegerField()
    
    def __str__(self):
        return self.rut
    