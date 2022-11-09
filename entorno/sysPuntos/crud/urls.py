from crud.views import CreateCliente, index, perfil, register
from django.urls import path, include
from crud.api.router import router_posts

urlpatterns = [
    path('', index, name="index"),
    path('api/', include(router_posts.urls)),
    path('register/', register, name="register"),
    path('perfil/', perfil, name="perfil"),
    path('CreateCliente/', CreateCliente, name="CreateCliente"),
]
