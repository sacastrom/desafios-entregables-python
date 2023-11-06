from django.contrib import admin
from controlgastos.models import CategoriaTransaccion, Transaccion, PresupuestoTransaccion, Mes

# Register your models here.

admin.site.register([CategoriaTransaccion, Transaccion, PresupuestoTransaccion, Mes])