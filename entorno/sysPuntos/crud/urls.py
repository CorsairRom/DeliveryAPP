from crud.views import index, perfil, register

from django.urls import path

urlpatterns = [
    path('', index, name="index"),
    path('register/', register, name="register"),
    path('perfil/', perfil, name="perfil"),
]
