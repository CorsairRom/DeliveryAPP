from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .form import ClienteForm

from crud.forms import Custom

# Create your views here.

def index(request):
    return render(request, 'crud/index.html')

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
    return render(request, 'registration/CreateCliente.html', context)