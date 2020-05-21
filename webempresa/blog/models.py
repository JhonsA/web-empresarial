from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Edición")

    class Meta: # Metadatos extendidos
        verbose_name = "categoría"
        verbose_name_plural = "categorías"
        ordering = ["-created"] # Ordenar por creacion, - sirve para hacer el reverso de la ordenacion de mas nuevo a mas antigio, de nuevos a mas antiguos

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    content = models.TextField(verbose_name="Contenido")
    published = models.DateTimeField(verbose_name="Fecha de publicación", default=now)
    image = models.ImageField(verbose_name="Imagen",upload_to="blog", null=True, blank=True)
    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name="Categorías", related_name="get_posts") # related_name para crear otros campos relacionados entre la categoria y un post he ir a buscarlos inversamente como yo quiera
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Edición")

    class Meta: # Metadatos extendidos
        verbose_name = "entrada"
        verbose_name_plural = "entradas"
        ordering = ["-created"] # Ordenar por creacion, - sirve para hacer el reverso de la ordenacion de mas nuevo a mas antigio, de nuevos a mas antiguos

    def __str__(self):
        return self.title
