from crud.views import index, register

from django.urls import path

urlpatterns = [
    path('', index, name="index"),
    path('register/', register, name="register"),
]
