from django.db import models

# Create your models here.

class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    subtitle = models.CharField(max_length=200, verbose_name="Subtítulo")
    content = models.TextField(verbose_name="Contenido")
    image = models.ImageField(verbose_name="Imagen", upload_to="services")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Edición")

    class Meta: # Metadatos extendidos
        verbose_name = "servicio"
        verbose_name_plural = "servicios"
        ordering = ["-created"] # Ordenar por creacion, - sirve para hacer el reverso de la ordenacion de mas nuevo a mas antigio, de nuevos a mas antiguos

    def __str__(self):
        return self.title