from django import forms
from controlgastos.models import CategoriaTransaccion

class CrearTransaccionFormulario(forms.Form):
    descripcion = forms.CharField(max_length=200)
    monto = forms.DecimalField(max_digits=10, decimal_places=2)
    tipo = forms.CharField(max_length=10) #gasto o ingreso
    categoria = forms.ModelChoiceField(queryset=CategoriaTransaccion.objects.all())
    
class CrearCategoriaFormulario(forms.Form):
    nombre = forms.CharField(max_length=200)
    
class CrearPresupuestoFormulario(forms.Form):
    categoria = forms.ModelChoiceField(queryset=CategoriaTransaccion.objects.all())
    presupuesto = forms.DecimalField(max_digits=10, decimal_places=2)
    gasto_real = forms.DecimalField(max_digits=10, decimal_places=2)