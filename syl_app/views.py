from django.urls import reverse_lazy
from django.views import View

from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic.detail import DetailView


from .models import Cruceros

# Basicamente creo el CRUD por medio de clases

class CrucerosBaseView(View):
    template_name = 'cruceros.html'
    model = Cruceros
    fields = '__all__'
    success_url = reverse_lazy('cruceros:all')


class CrucerosListView(CrucerosBaseView,ListView):
    """
    ESTO ME PERMITE CREAR UNA VISTA CON LOS VIAJES
    """
    ...

class CrucerosDetailView(CrucerosBaseView,DetailView):
    model = Cruceros
    template_name = "cruceros_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        crucero = get_object_or_404(Cruceros, pk=self.kwargs['pk'])
        context['compania_imagen'] = crucero.companias_imagenes.get(crucero.compania)
        return context

class CrucerosCreateView(CrucerosBaseView,CreateView):
    template_name = "cruceros_create.html"
    extra_context = {
        "tipo": "Crear viaje"
    }


class CrucerosUpdateView(CrucerosBaseView,UpdateView):
    template_name = "cruceros_create.html"
    extra_context = {
        "tipo": "Actualizar"
    }

class CrucerosDeleteView(DeleteView):
# Personalización de la vista DeleteView para que pueda manejar la solicitud DELETE

    model = Cruceros
    success_url = reverse_lazy('cruceros:all') 

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        
        # Devuelve una respuesta JSON exitosa 
        return JsonResponse({'message': 'Registro eliminado correctamente'}, status=200)
