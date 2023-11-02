from django.urls import path
from controlgastos.views import inicio, categoria_transaccion, transaccion, presupuesto_transaccion, mes

urlpatterns = [
    path('', inicio),
    path('categoria-transaccion/', categoria_transaccion),
    path('transaccion/', transaccion),
    path('presupuesto-transaccion/', presupuesto_transaccion),
    path('mes/', mes)
]