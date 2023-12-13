from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View

from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic.detail import DetailView


from .models import Viajes


class ViajesBaseView(View):
    template_name = 'viajes.html'
    model = Viajes
    fields = '__all__'
    success_url = reverse_lazy('viajes:all')


class ViajesListView(ViajesBaseView,ListView):
    """
    ESTO ME PERMITE CREAR UNA VISTA CON LOS VINOS
    """
class ViajesDetailView(ViajesBaseView,DetailView):
    template_name = "viajes_detail.html"

class ViajesCreateView(ViajesBaseView,CreateView):
    template_name = "viajes_create.html"
    extra_context = {
        "tipo": "Crear viaje"
    }


class ViajesUpdateView(ViajesBaseView,UpdateView):
    template_name = "viajes_create.html"
    extra_context = {
        "tipo": "Actualizar viaje"
    }

class ViajesDeleteView(ViajesBaseView,DeleteView):
    template_name = "viajes_delete.html"
    extra_context = {
        "tipo": "Borrar viaje"
    }
