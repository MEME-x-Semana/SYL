from django.db import models
from django.db.models import Model


class Viajes(Model):
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

    companias_imagenes = {
        "MSC": "https://res.cloudinary.com/dciovdqaf/image/upload/v1702415670/MSC_g2ofl3.jpg",
        "RYG": "https://res.cloudinary.com/dciovdqaf/image/upload/v1702420502/RYG_a2pjfx.jpg",
        "Viking": "https://res.cloudinary.com/dciovdqaf/image/upload/v1702420502/Viking_gnf7yt.jpg",
        "NCL": "https://res.cloudinary.com/dciovdqaf/image/upload/v1702420502/NCL_qwwb5n.jpg",
        "Seabourn": "https://res.cloudinary.com/dciovdqaf/image/upload/v1702420502/Seabourn_op6kwg.jpg",
        "Star Cruises": "https://res.cloudinary.com/dciovdqaf/image/upload/v1702420501/Star_Cruises_vbbtth.webp",
        "Carnival": "https://res.cloudinary.com/dciovdqaf/image/upload/v1702420501/Carnival_ax7q9x.jpg",
        "Costa": "https://res.cloudinary.com/dciovdqaf/image/upload/v1702420501/Costa_jnoysj.jpg",
        "AIDA": "https://res.cloudinary.com/dciovdqaf/image/upload/v1702420502/AIDA_cky4ot.jpg",
    }

    compania = models.CharField(max_length=100, choices=companias_choices, default=companias_choices[0][0])
    continente = models.CharField(max_length=100, choices=continentes_choices, default=continentes_choices[0][0])
    precio = models.FloatField(null=False, blank=False, default=5000)
    puerto = models.CharField(max_length=100, choices=puertos_choices, default=puertos_choices[0][0])


    @property
    def imagen_compania(self):
        return self.companias_imagenes.get(self.compania, None)

    # metadata
    class Meta:
        db_table = "cruise_table"
        verbose_name = "Viaje"
        verbose_name_plural = "Viajes"
        ordering = ["id"]

    def __str__(self):
        return f"La compañía {self.compania} tiene viajes a {self.continente}"

    def get_fields(self):
        return [
            (field.verbose_name, field.value_from_object(self))
            for field in self.__class__._meta.fields[1:]
        ]
