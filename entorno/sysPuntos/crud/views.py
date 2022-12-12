import random

from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

from crud.Carrito import Carrito
from crud.Lista import Listado
from crud.context_processor import total_carrito
from .forms import Custom, ClienteForm, DireccionesForm
from .models import cliente, detalle_pedido, direccion, metodo_pago, pedido, producto, trabajador, local
from django.db import connection
import logging
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
import requests


# Create your views here.


# get data client
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
    
    # if 'copy-data' in request.POST:
    #     print("estoy  en el copy-data")
    #     response_mealdb = requests.get('https://www.themealdb.com/api/json/v1/1/categories.php')
    #     categories = response_mealdb.json()
    #     cat = categories["categories"]

    #     def randomPrice():
    #         precio = random.randrange(3500, 12000, 100)
    #         return precio
    #     def randomStock():
    #         stock = random.randrange(1, 30, 1)
    #         return stock

    #     for item in cat:
    #         strCategory = item['strCategory']
    #         reponse_strCategory = requests.get(f'https://www.themealdb.com/api/json/v1/1/filter.php?c={strCategory}')
    #         meals = reponse_strCategory.json()
    #         meals_index = meals['meals']
    #         for meal in meals_index:
    #             print(meal['idMeal'])
    #             print(meal['strMeal'])
    #             print(randomPrice())
    #             print(randomStock())
                
    #             pro = producto()
    #             pro.id = meal['idMeal']
    #             pro.nom_producto = meal['strMeal']
    #             pro.precio = int(randomPrice())
    #             pro.stock = int(randomStock())
    #             pro.save()
    #             print("------------")
    #             print("Agregado!")
                
    
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
    dir = direccion.objects.filter(cliente_dir = client)
    texto = "prueba"
    
    
    if 'cambiar' in request.POST:
        texto = request.POST.get('dir')
        direccion_id = request.POST.get("recipient-id")
        dir_mod= direccion.objects.get(id = direccion_id)
        dir_mod.nombre_dir = texto
        dir_mod.save()
        print(dir_mod)
        # redirect(perfil)
        
    if 'eliminar' in request.POST:
        direccion_idd = request.POST.get("recipient-id")
        dir_del= direccion.objects.get(id = direccion_idd)
        dir_del.delete()
        
        
        
        
    data = {
        "cliente": client,
        "direccion": dir,
        "texto": texto
    }
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
    if 'pedir' in request.GET:
        print("boton precionado pedir")
        
    data = {
        'food':meals['meals']
    }
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

    



def comprar (request):
    if 'cambiar' in request.POST:
        texto = str(request.POST['dir'] )
        print("boton precionado cambiar")
        print(texto)
        redirect(perfil)
    ctx = {
        
    }
    
    return render(request, 'crud/compra.html', ctx)

# carro de compras

def carro(request):
    client = cliente.objects.get(username_id = request.user.id)
    ctx = {
        
    }
    return render(request, "crud/carro.html", ctx)

def eliminar(request, id):
    product = get_object_or_404(producto, id=id)
    product.delete()
    return redirect(perfil, 2)

def agregar(request, producto_id):
    carrito = Carrito(request)
    product = producto.objects.get(id=producto_id)
    carrito.agregar(product)
    return redirect(categoria)

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    product = producto.objects.get(id=producto_id)
    carrito.eliminar(product)
    return redirect("carro")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    product = producto.objects.get(id=producto_id)
    carrito.restar(product)
    return redirect("carro")

def sumar_producto(request, producto_id):
    carrito = Carrito(request)
    product = producto.objects.get(id=producto_id)
    carrito.sumar(product)
    return redirect("carro")
    
def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("carro")

def guardar(request):
    usuario = request.user
    tot_carrito = total_carrito(request)
    carrito = Carrito(request)
    total = tot_carrito["total_carrito"]
    client = cliente.objects.get(username_id = usuario.id)
    trab = trabajador.objects.get(rut_trabajador = '18200400-1')
    loc = local.objects.get(id = 2)
    pago = metodo_pago.objects.get(id =2)
    venta = pedido()
    venta.rut_cliente = client
    venta.rut_trabajador = trab
    venta.id_local = loc
    venta.id_tipo_pago = pago
    venta.estado = 'Pagado'
    venta.calificacion = 5
    venta.total = total
    venta.save()
    venta_actual = pedido.objects.get(id = venta.id)
    if "carrito" in request.session.keys():
        for key, value in request.session["carrito"].items():
            product = producto.objects.get(id = int(value["producto_id"]))
            pedid = pedido.objects.get(id = venta_actual.id)
            detalle = detalle_pedido(id_pedido = pedid, id_producto = product, cantidad = int(value["cantidad"]), precio = int(value["precio"]) )
            detalle.save()
            
    carrito.limpiar()
    return redirect(perfil)  

def historial(request):
    user = request.user
    client = cliente.objects.get(username_id=user.id)
    ventas = pedido.objects.filter(rut_cliente = client.rut_cliente)
    ctx = {
        "ventas":ventas,
    }
    
    return render(request, 'crud/historial.html', ctx)

def borrar_registro(request, venta_id):
    venta = pedido.objects.get(id = venta_id) 
    venta.delete()
    return redirect(historial)

def ver_detalle(request, venta_id):
    
    # detalle_venta = detalle_pedido.objects.filter(id_pedido = venta_id)
    # print(str(detalle_venta[0]))
    
    detalle_venta = detalle_pedido
    productos = producto
    pro = producto.objects.get(id = 52894)
    listado = Listado(request)
    print(pro)
    listado.agregar(productos, venta_id, detalle_venta)
    
    return  redirect(historial)

def limpiar_lista(request, venta_id):
    detalle_venta = detalle_pedido
    
    lista = Listado(request)
    lista.limpiar(detalle_venta, venta_id)
    return redirect(historial)