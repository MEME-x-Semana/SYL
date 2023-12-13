from django.db import models


# Create your models here.
class Viajes(models.Model):
    nombre = models.CharField(
        max_length=200, null=False, unique=True, verbose_name="Nombre"
    )
    rating = models.PositiveSmallIntegerField(blank=False, null=False)
    abv = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = "viajes_table"
        verbose_name = "Viaje"
        verbose_name_plural = "Viajes"
        ordering = ["id"]

    def __str__(self):
        return f"Viaje: {self.nombre}, Rating: {self.abv}"

    def get_fields(self):
        return [
            (field.verbose_name, field.value_from_object(self))
            for field in self.__class__._meta.fields[1:]
        ]
