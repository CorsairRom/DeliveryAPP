from crud.views import  CreateCliente, agregar, carro, eliminar, eliminar_producto, index, limpiar_carrito, perfil, register, categoria, food, restar_producto, setDireccion, comprar, sumar_producto
from django.urls import path, include
from crud.api.router import router_posts

urlpatterns = [
    path('', index, name="index"),
    path('api/', include(router_posts.urls)),
    path('register/', register, name="register"),
    path('perfil/', perfil, name="perfil"),
    path('CreateCliente/', CreateCliente, name="CreateCliente"),
    path('categoria/', categoria, name="categoria"),
    path('food/<name>', food, name="food"),
    path('direccion/', setDireccion, name="direccion"),
    path('comprar/', comprar, name="comprar"),
    path('carro/', carro, name="carro"),
    path('eliminar/<id>/', eliminar, name="eliminar"),
    path('agregar/<int:producto_id>/<str:pagina>/', agregar, name="agregar"),
    path('eliminar/<int:producto_id>/', eliminar_producto, name="eliminar"),
    path('restar/<int:producto_id>/', restar_producto, name="restar"),
    path('sumar/<int:producto_id>/', sumar_producto, name="sumar"),
    path('limpiar/', limpiar_carrito, name="limpiar"),
]
