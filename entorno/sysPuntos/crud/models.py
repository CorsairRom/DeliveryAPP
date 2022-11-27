from django.db import models
from django.contrib.auth.models import User

# Create your models here.
 
class cliente(models.Model):
    rut_cliente = models.CharField(unique=True, max_length = 10, primary_key=True, verbose_name='Rut')
    username = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank = True)
    direccion_cli = models.CharField( max_length = 50, verbose_name='Direccion Principal')
    nombre = models.CharField(max_length = 30)
    apellido_pa = models.CharField(max_length = 30, verbose_name='Apellido Paterno')
    apellido_ma = models.CharField(max_length = 30, verbose_name='Apellido Materno')
    
    def __str__(self):
        return self.rut_cliente
    
class direccion(models.Model):
    nombre_dir = models.CharField(max_length = 50, verbose_name='Nombre direcion')
    descripcion = models.TextField()
    cliente_dir = models.ForeignKey(cliente, on_delete = models.CASCADE, null = True, blank = True, verbose_name='Direccion cliente')
    def __str__(self):
        return self.nombre_dir
    
class usuarioPrueba(models.Model):
    rut = models.CharField(max_length = 50)
    id_tipo_usuario = models.IntegerField()
    
    def __str__(self):
        return self.rut
    
class local(models.Model):
    nombre_local = models.CharField(max_length=50, unique= True, null=True, verbose_name='nombre')
    direccion_local = models.CharField(max_length=200, null=True, verbose_name='direccion')
    
    def __str__(self):
        return self.nombre_local
    
class promocion(models.Model):
    id_local = models.ForeignKey(local, on_delete=models.CASCADE)
    descripcion_promo = models.TextField(max_length=50, null=True, verbose_name='Descripcion')
    nombre_promo = models.CharField(max_length=50 , null=True, verbose_name='nombre')
    fecha_ini = models.DateField(auto_now_add=False, null=True, verbose_name='fecha inicio')
    fecha_fin = models.DateField(auto_now_add=False, null=True, verbose_name='fecha fin')
    
    def __str__(self):
        return self.nombre_promo

class metodo_pago(models.Model):
    nom_pago = models.CharField(max_length=50, null=True, verbose_name='Nombre Metodo')
    
    def __str__(self):
        return self.nom_pago
    
class producto(models.Model):
    nom_producto = models.CharField(max_length=50, null=True, verbose_name='Nombre producto') 
    precio = models.IntegerField()
    stock = models.IntegerField()
    
    def __str__(self):
        return self.nom_producto

class trabajador(models.Model):
    rut_trabajador = models.CharField(max_length=10, null=True, primary_key=True, verbose_name='Rut')
    nombre_trabajador = models.CharField(max_length=50, null=True, verbose_name='Nombre trabajador')
    tipo_trabajador = models.CharField(max_length=50, null=True, verbose_name='Tipo trabajador')
    
    def __str__(self):
        return self.rut_trabajador

   
class pedido(models.Model):
    rut_cliente = models.ForeignKey(cliente, on_delete=models.CASCADE,null=True, verbose_name='Rut cliente')
    rut_trabajador = models.ForeignKey(trabajador, on_delete=models.CASCADE, null=True, verbose_name='Rut trabajador')
    id_local = models.ForeignKey(local, on_delete=models.CASCADE, null=True, verbose_name='Id local')
    id_tipo_pago = models.ForeignKey(metodo_pago, on_delete=models.CASCADE, null=True, verbose_name='Metodo de pago')
    fecha = models.DateField(auto_now_add=False, null=True)
    estado = models.CharField(max_length=30, null=True)
    calificacion = models.IntegerField()
    
    def __str__(self):
        return self.id
         
    
class detalle_pedido(models.Model):
    id_producto = models.ForeignKey(producto, null=True, on_delete=models.CASCADE)
    id_pedido = models.ForeignKey( pedido, on_delete=models.CASCADE, null=True)
    cantidad = models.IntegerField()
    
    def __str__(self):
        return self.id