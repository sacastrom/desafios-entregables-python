from django.urls import path
from controlgastos.views import inicio, categoria_transaccion, transaccion, presupuesto_transaccion, mes, crear_transaccion, crear_categoria, crear_presupuesto

urlpatterns = [
    path('', inicio, name='inicio'),
    path('categoria-transaccion/', categoria_transaccion, name='categoria'),
    path('transaccion/', transaccion, name='transaccion'),
    path('presupuesto-transaccion/', presupuesto_transaccion, name='presupuesto'),
    path('mes/', mes, name='mes'),
    path('transaccion/crear/', crear_transaccion, name='crear_transaccion'),
    path('categoria-transaccion/crear/', crear_categoria, name='crear_categoria'),
    path('presupuesto-transaccion/crear/', crear_presupuesto, name='crear_presupuesto'),
]