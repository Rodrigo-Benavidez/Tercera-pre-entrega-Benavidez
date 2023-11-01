from django.urls import path
from inicio.views import inicio, zapatillas, crear_zapatilla

urlpatterns = [
    path('', inicio, name='inicio'),
    path('zapatillas/', zapatillas, name='zapatillas'),
    path('zapatillas/crear/', crear_zapatilla, name='crear_zapatilla')    
]