from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .form import ClienteForm
from .models import cliente
from django.db import connection

from crud.forms import Custom

# Create your views here.

def get_data():
    django_cursor = connection.cursor()
    int_cursor = django_cursor.connection.cursor()
    out_cursor = django_cursor.connection.cursor()
    
    django_cursor.callproc("sp_get_user", [out_cursor])
    lista = []
    for fila in out_cursor:
        lista.append(fila)
    
    return lista



def index(request):
    data = {
        'cli': get_data()
    }
    return render(request, 'crud/index.html', data)

def register(request):
    data = {
        "form": Custom
    }
    if request.method == 'POST':
        formulario = Custom(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            #redirigir al inicio
            user = authenticate(username= formulario.cleaned_data["username"], password = formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to="cliente")
        data["form"]= formulario    
    return render(request, 'registration/register.html', data)

def perfil(request):
    
    return render(request, 'crud/perfil.html')

def CreateCliente(request):
    form = ClienteForm
    context = {
        "form": form
    }
    if request.method == 'POST':
        if form.is_valid():
            datos = form.cleaned_data
            cli = cliente()
            cli.username = request.user
            cli.rut_cliente = datos.get("rut_cliente")
            cli.direccion_cli = datos.get("direccion_cli")
            cli.nombre = datos.get ("nombre")
            cli.apellido_pa = datos.get("apellido_pa")
            cli.apellido_ma = datos.get("apellido_ma")
            cli.save()
            return redirect(perfil)
    return render(request, 'registration/CreateCliente.html', context)