from django.urls import reverse_lazy
from django.views import View

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
    template_name = "cruceros_detail.html"

class CrucerosCreateView(CrucerosBaseView,CreateView):
    template_name = "cruceros_create.html"
    extra_context = {
        "tipo": "Crear viaje"
    }


class CrucerosUpdateView(CrucerosBaseView,UpdateView):
    template_name = "cruceros_create.html"
    extra_context = {
        "tipo": "Actualizar viaje"
    }

class CrucerosDeleteView(CrucerosBaseView,DeleteView):
    template_name = "cruceros_delete.html"
    extra_context = {
        "tipo": "Borrar viaje"
    }

