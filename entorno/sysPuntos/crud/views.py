from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import Custom, ClienteForm, DireccionesForm
from .models import cliente, direccion
from django.db import connection
import logging
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
import requests


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
    
    
    data1 = {}
    data2 = {}
    data3 = {}
    for x in range(1,4):
        response = requests.get('https://www.themealdb.com/api/json/v1/1/random.php')
        meal = response.json()
        if x==1: data1.update(meal);
        if x==2: data2.update(meal);
        if x==3: data3.update(meal);

    random1 = data1['meals']
    random2 = data2['meals']
    random3 = data3['meals']
    
    data = {
        'cli': get_data(),
        'random1': random1,
        'random2': random2,
        'random3': random3
    }
    return render(request, 'crud/index.html', data)

def register(request):
    data = {
        "form": Custom
    }
    if request.method == "POST":
        formulario = Custom(data=request.POST)
        if formulario.is_valid():
            prueba = formulario.save()
            dataform = formulario.cleaned_data
            usr = dataform.get("username")
            psw = dataform.get("password1")
            user = authenticate(username= usr, password = psw)
            login(request, prueba)
            # print("esto es un print")
            return redirect(to="CreateCliente")
        data["form"]= formulario    
    return render(request, 'registration/register.html', data)

def perfil(request):
    client = cliente.objects.get(username_id = request.user.id)
    data = {
        "cliente": client
    }
    print(client.nombre)
    return render(request, 'crud/perfil.html', data)

def CreateCliente(request):
    
    context = {
        "form": ClienteForm
    }
    if request.method == 'POST':
        form = ClienteForm(data=request.POST)
        if form.is_valid():
            form.save()
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

def categoria(request):
    response = requests.get('https://www.themealdb.com/api/json/v1/1/categories.php')
    category = response.json()
    
    data = {
        'categorias' : category['categories'],
        
    }
    # print(category['categories'])
    # for item in category['categories']:
    #     print(item['idCategory'])
    return render( request, 'crud/categoria.html', data)

def food (request, name):
    reponse = requests.get(f'https://www.themealdb.com/api/json/v1/1/filter.php?c={name}')
    meals = reponse.json()
    data = {
        'food':meals['meals']
    }
    # print(meals['meals'])
    
    return render(request, 'crud/food.html', data)

def setDireccion (request):
    client = cliente.objects.get(username_id = request.user.id)
    ctx ={
        "form": DireccionesForm
    }
    if request.method == "POST":
        form = DireccionesForm(data = request.POST)
        if form.is_valid():
            form.save()
            datos = form.cleaned_data
            dir = direccion()
            dir.nombre_dir=datos.get('nombre_dir')
            dir.descripcion = datos.get('descripcion')
            dir.cliente_dir = client
            dir.save()
            return redirect(perfil)
    return render(request, 'crud/direccion.html', ctx)