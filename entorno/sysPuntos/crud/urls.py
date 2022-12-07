from crud.views import  CreateCliente, index, perfil, register, categoria, food, setDireccion
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
    path('direccion/', setDireccion, name="direccion")
]
