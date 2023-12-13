from django.urls import reverse_lazy
from django.views import View

from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic.detail import DetailView


from .models import Viajes

# Basicamente creo el CRUD por medio de clases

class ViajesBaseView(View):
    template_name = 'viajes.html'
    model = Viajes
    fields = '__all__'
    success_url = reverse_lazy('viajes:all')


class ViajesListView(ViajesBaseView,ListView):
    """
    ESTO ME PERMITE CREAR UNA VISTA CON LOS VIAJES
    """
    ...

class ViajesDetailView(ViajesBaseView,DetailView):
    model = Viajes
    template_name = "viajes_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        crucero = get_object_or_404(Viajes, pk=self.kwargs['pk'])
        context['compania_imagen'] = crucero.companias_imagenes.get(crucero.compania)
        return context

class ViajesCreateView(ViajesBaseView,CreateView):
    template_name = "viajes_create.html"
    extra_context = {
        "tipo": "Crear viaje"
    }


class ViajesUpdateView(ViajesBaseView,UpdateView):
    template_name = "viajes_create.html"
    extra_context = {
        "tipo": "Actualizar"
    }

class ViajesDeleteView(DeleteView):
# Personalización de la vista DeleteView para que pueda manejar la solicitud DELETE

    model = Viajes
    success_url = reverse_lazy('viajes:all') 

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        
        # Devuelve una respuesta JSON exitosa 
        return JsonResponse({'message': 'Registro eliminado correctamente'}, status=200)
