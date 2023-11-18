from django.urls import path
from campera.views import ListadoCamperas, CrearCampera, ActualizarCampera, EliminarCampera, DetalleCampera

urlpatterns = [
    path('camperas/', ListadoCamperas.as_view(), name='camperas'),
    path('camperas/crear/', CrearCampera.as_view(), name='crear_campera'),
    path('camperas/<int:pk>/', DetalleCampera.as_view(), name='detalle_campera'),
    path('camperas/<int:pk>/actualizar/', ActualizarCampera.as_view(), name='actualizar_campera'),
    path('camperas/<int:pk>/eliminar/', EliminarCampera.as_view(), name='eliminar_campera'),
]
