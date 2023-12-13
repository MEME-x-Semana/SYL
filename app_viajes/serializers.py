from rest_framework.serializers import ModelSerializer
from .models import Viajes

class ViajesSerializer(ModelSerializer):
    class Meta:
        model = Viajes
        fields = "__all__"