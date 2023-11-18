from django.urls import path
from inicio.views import inicio, zapatillas, crear_zapatilla, eliminar_zapatilla, actualizar_zapatilla, detalle_zapatilla, about_me

urlpatterns = [
    path('', inicio, name='inicio'),
    path('about_me/', about_me, name='about_me'),
    path('zapatillas/', zapatillas, name='zapatillas'),
    path('zapatillas/crear/', crear_zapatilla, name='crear_zapatilla'), 
    path('zapatillas/<int:zapatilla_id>/', detalle_zapatilla, name='detalle_zapatilla'),
    path('zapatillas/<int:zapatilla_id>/eliminar/', eliminar_zapatilla, name='eliminar_zapatilla'),
    path('zapatillas/<int:zapatilla_id>/actualizar/', actualizar_zapatilla, name='actualizar_zapatilla'),
]