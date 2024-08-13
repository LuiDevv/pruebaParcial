from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Producto


def mostrar_template(request):
    return render(request, 'miPrimerTemplate.html')
# Create your views here.

def Productos(request):
    #return HttpResponse("Nuestra primera vista!")
    misProductos = Producto.objects.all().values()

    template = loader.get_template('productos.html')
    context = {
        'misProductos': misProductos,
    }
    return HttpResponse(template.render(context, request))

def BienvenidaProductos(request):
    template = loader.get_template('miPrimerTemplate.html')
    return HttpResponse(template.render())


from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


from django.conf.urls import handler404
from django.shortcuts import render

def test(request):
    return render(request, '404.html')
