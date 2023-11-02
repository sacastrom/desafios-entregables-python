from django.shortcuts import render
from controlgastos.models import CategoriaTransaccion

# Create your views here.

def inicio(request):
    return render(request, 'controlgastos/inicio.html', {})

def categoria_transaccion(request):
    categoria = CategoriaTransaccion(nombre='Ropa')
    categoria.save()
    
    return render(request, 'controlgastos/categoria_transaccion.html', {'categoria': categoria} )

def transaccion(request):
    
    return render(request, 'controlgastos/transaccion.html', {} )

def presupuesto_transaccion(request):
    
    return render(request, 'controlgastos/presupuesto_transaccion.html', {} )

def mes(request):
    
    return render(request, 'controlgastos/mes.html', {} )