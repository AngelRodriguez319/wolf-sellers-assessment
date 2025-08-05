from django.db import models

from base.models import UUIDModel, TimeStampedModel


class Product(UUIDModel, TimeStampedModel):

    name = models.CharField(max_length=255, verbose_name="Nombre")
    description = models.TextField(blank=True, null=True, verbose_name="Descripción")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    available = models.BooleanField(default=True, verbose_name="¿Disponible?")

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ["name"]

    def __str__(self):
        return self.name

