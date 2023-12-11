from django.db import models
from django.db.models import Model


# Create your models here.
class Cruceros(Model):
    companias_choices = [
        ("MSC", "MSC"),
        ("RYG", "RYG"),
        ("Viking", "Viking"),
        ("NCL", "NCL"),
        ("Seabourn", "Seabourn"),
        ("Star Cruises", "Star Cruises"),
        ("Carnival", "Carnival"),
        ("Costa", "Costa"),
        ("AIDA", "AIDA"),
    ]

    continentes_choices = [
        ("Sudamerica", "Sudamerica"),
        ("Caribe", "Caribe"),
        ("Europa", "Europa"),
        ("Asia", "Asia"),
    ]

    puertos_choices = [
        ("Palermo", "Palermo"),
        ("Bari", "Bari"),
        ("Barcelona", "Barcelona"),
        ("Valencia", "Valencia"),
        ("Marsella", "Marsella"),
        ("Lorient", "Lorient"),
        ("La Habana", "La Habana"),
        ("Puerto Príncipe", "Puerto Príncipe"),
        ("Kingston", "Kingston"),
        ("Hong Kong", "Hong Kong"),
        ("Tokio", "Tokio"),
        ("Buenos Aires", "Buenos Aires"),
        ("Ushuaia", "Ushuaia"),
        ("Rio de Janeiro", "Rio de Janeiro"),
        ("Recife", "Recife"),
    ]

    compania = models.CharField(max_length=100, choices=companias_choices)
    continente = models.CharField(max_length=100, choices=continentes_choices)
    precio = models.FloatField(null=False, blank=False, default=5000)
    puerto = models.CharField(max_length=100, choices=puertos_choices)

    # metadata
    class Meta:
        db_table = "cruise_table"

    def __str__(self):
        return f"La compañía {self.compania} tiene viajes a {self.continente}"

    def get_fields(self):
        return [
            (field.verbose_name, field.value_from_object(self))
            for field in self.__class__._meta.fields[1:]
        ]
