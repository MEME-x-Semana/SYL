from .models import Cruceros
from django.contrib import admin
from django.contrib.admin import ModelAdmin

# Register your models here.

@admin.register(Cruceros)
class CrucerosAdmin(ModelAdmin):
    ...