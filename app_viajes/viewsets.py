from rest_framework.viewsets import ModelViewSet
from .models import Viajes
from .serializers import ViajesSerializer

class ViajesViewSet(ModelViewSet):
    queryset = Viajes.objects.all()
    serializer_class = ViajesSerializer