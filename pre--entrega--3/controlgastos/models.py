from django.db import models

# Create your models here.
class CategoriaTransaccion(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __str__(self):
        return f'{self.id} - {self.nombre}'

class Transaccion(models.Model):
    descripcion = models.CharField(max_length=200)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)
    tipo = models.CharField(max_length=10) #gasto o ingreso
    categoria_transaccion = models.ForeignKey(CategoriaTransaccion, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.id} - {self.descripcion} - {self.monto} - {self.fecha} - {self.tipo} - {self.categoria_transaccion}'
    
    
class PresupuestoTransaccion(models.Model):
    categoria_transaccion = models.ForeignKey(CategoriaTransaccion, on_delete=models.CASCADE)
    presupuesto = models.DecimalField(max_digits=10, decimal_places=2)
    gasto_real = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    def __str__(self):
        return f'{self.id} - {self.categoria_transaccion} - {self.presupuesto} - {self.gasto_real}'
    
class Mes(models.Model):
    anio = models.IntegerField()
    mes = models.IntegerField()
    
    