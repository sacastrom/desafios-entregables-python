from django.shortcuts import render
from controlgastos.models import CategoriaTransaccion, Transaccion
from controlgastos.forms import CrearTransaccionFormulario

# Create your views here.

def inicio(request):
    return render(request, 'controlgastos/inicio.html', {})

def categoria_transaccion(request):
    
    return render(request, 'controlgastos/categoria_transaccion.html', {} )

def transaccion(request):
    
    return render(request, 'controlgastos/transaccion.html', {} )

def presupuesto_transaccion(request):
    
    return render(request, 'controlgastos/presupuesto_transaccion.html', {} )

def mes(request):
    
    return render(request, 'controlgastos/mes.html', {} )

def crear_transaccion(request):
    """ print(request.POST)
    
    if request.method == 'POST':
        descripcion = request.POST.get('descripcion')
        monto = request.POST.get('monto')
        tipo = request.POST.get('tipo')
        categoria = CategoriaTransaccion.objects.get(nombre='Ropa')
        
        
        transaccion = Transaccion(descripcion=descripcion, monto=monto, tipo=tipo, categoria_transaccion=categoria)
        transaccion.save() """
        
    if request.method == 'POST':
        formulario = CrearTransaccionFormulario(request.POST)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
            
            descripcion = info_limpia.get('descripcion')
            monto = info_limpia.get('monto')
            tipo = info_limpia.get('tipo')
            categoria = info_limpia.get('categoria')
        
        
            transaccion = Transaccion(descripcion=descripcion, monto=monto, tipo=tipo, categoria_transaccion=categoria)
            transaccion.save()
    else: 
        formulario = CrearTransaccionFormulario()
    return render(request, 'controlgastos/crear_transaccion.html', {'formulario': formulario})