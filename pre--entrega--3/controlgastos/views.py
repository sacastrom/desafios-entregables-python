from django.shortcuts import render
from controlgastos.models import CategoriaTransaccion, Transaccion, PresupuestoTransaccion
from controlgastos.forms import CrearTransaccionFormulario, CrearCategoriaFormulario, CrearPresupuestoFormulario

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

def crear_categoria(request):        
    if request.method == 'POST':
        formulario = CrearCategoriaFormulario(request.POST)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
            
            nombre = info_limpia.get('nombre')
            
        
        
            categoria = CategoriaTransaccion(nombre=nombre)
            categoria.save()
    else: 
        formulario = CrearCategoriaFormulario()
    return render(request, 'controlgastos/crear_categoria.html', {'formulario': formulario})

def crear_presupuesto(request):        
    if request.method == 'POST':
        formulario = CrearPresupuestoFormulario(request.POST)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
            
            presupuesto = info_limpia.get('presupuesto')
            gasto_real = info_limpia.get('gasto_real')
            categoria = info_limpia.get('categoria')
            
        
            presupuesto_transaccion = PresupuestoTransaccion(categoria_transaccion=categoria, presupuesto=presupuesto, gasto_real=gasto_real)
            presupuesto_transaccion.save()
    else: 
        formulario = CrearPresupuestoFormulario()
    return render(request, 'controlgastos/crear_presupuesto.html', {'formulario': formulario})