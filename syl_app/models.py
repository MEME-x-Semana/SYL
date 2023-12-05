from django.db import models
from django.db.models import Model

# Create your models here.
class Cruceros(Model):
    """
    Atributos de clase que son usadas por herencia de la clase Model

    """
    companias_choices = [
      ("ID 1: MSC", "MSC"),
      ("ID 2: RYG", "RYG"),
      ("ID 3: Viking", "Viking"),
      ("ID 4: NCL", "NCL"),
      ("ID 5: Seabourn", "Seabourn"),
      ("ID 6: Star Cruises", "Star Cruises"),
      ("ID 7: Carnival", "Carnival"),
      ("ID 8: Costa", "Costa"),
      ("ID 9: AIDA", "AIDA")
    ]
    
    continentes_choices = [
      ("ID 1: Sudamerica", "Sudamerica"),
      ("ID 2: Caribe", "Caribe"),
      ("ID 3: Europa", "Europa"),
      ("ID 4: Asia", "Asia")
    ]

    puertos_choices = [
      ("ID 1: Palermo", "Palermo"),
      ("ID 2: Bari", "Bari"),
      ("ID 3: Barcelona", "Barcelona"),
      ("ID 4: Valencia", "Valencia"),
      ("ID 5: Marsella", "Marsella"),
      ("ID 6: Lorient", "Lorient"),
      ("ID 7: La Habana", "La Habana"),
      ("ID 8: Puerto Príncipe", "Puerto Príncipe"),
      ("ID 9: Kingston", "Kingston"),
      ("ID 10: Hong Kong", "Hong Kong"),
      ("ID 11: Tokio", "Tokio"),
      ("ID 12: Buenos Aires", "Buenos Aires"),
      ("ID 13: Ushuaia", "Ushuaia"),
      ("ID 14: Rio de Janeiro", "Rio de Janeiro"),
      ("ID 15: Recife", "Recife")
    ]
    
    
    compania   = models.CharField(max_length=100, choices=companias_choices)
    continente = models.CharField(max_length=100, choices=continentes_choices)
    precio     = models.FloatField(null=False, blank=False, default=5000) 
    puerto     = models.CharField(max_length=100, choices=puertos_choices)


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
