from django.db import models
from django.db.models import Model

# Create your models here.
class Cruceros(Model):
    """
    Atributos de clase que son usadas por herencia de la clase Model

    """
    continentes_choices = [
      ("Sudamerica"),
      ("Caribe"),
      ("Europa"),
      ("Asia")
    ]

    compania   = models.CharField(max_length=100, default="Compañía X")
    continente = models.CharField(max_length=100, default="Continente X")
    precio     = models.FloatField(null=False, blank=False, default=5000) 
    puerto     = models.CharField(max_length=100, choices=continentes_choices)


    #metadata
    class Meta:
      db_table = "cruise_table"


    def __str__(self):
        return f"La compañía {self.compania} tiene viajes a {self.continente}"

    def get_fields(self):
        return [
            (field.verbose_name, field.value_from_object(self))
            for field in self.__class__._meta.fields[1:]
        ]
