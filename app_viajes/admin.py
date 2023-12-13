from django.contrib import admin
from .models import Viajes
# Register your models here.
@admin.register(Viajes)
class ViajesAdmin(admin.ModelAdmin):
    ...