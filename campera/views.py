from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from campera.models import Campera
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class ListadoCamperas(ListView):
    model = Campera
    context_object_name = 'listado_de_camperas'
    template_name = 'campera/camperas.html'
    
    def get_queryset(self):
        color = self.request.GET.get('color', '')
        if color:
            listado_de_camperas = self.model.objects.filter(color__icontains=color)
        else:
            listado_de_camperas = self.model.objects.all()
        return listado_de_camperas

class CrearCampera(LoginRequiredMixin, CreateView):
    model = Campera
    template_name = "campera/crear_campera.html"
    fields = ['talle', 'color', 'descripcion', 'fecha_creacion']
    success_url = reverse_lazy('camperas')
    
class ActualizarCampera(LoginRequiredMixin, UpdateView):
    model = Campera
    template_name = "campera/actualizar_campera.html"
    fields = ['talle', 'color', 'descripcion', 'fecha_creacion']
    success_url = reverse_lazy('camperas')
    
class DetalleCampera(DetailView):
    model = Campera
    template_name = "campera/detalle_campera.html"

class EliminarCampera(LoginRequiredMixin, DeleteView):
    model = Campera
    template_name = "campera/eliminar_campera.html"
    success_url = reverse_lazy('camperas')
