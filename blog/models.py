from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User 

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "categoría"
        verbose_name_plural = "categorías"

    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    content = models.TextField(null=True, blank=True, verbose_name="Contenido")
    published = models.DateTimeField(default=now,verbose_name="Fecha de publicacion")
    image = models.ImageField(null=True, blank=True, verbose_name="Imagen", upload_to="blog")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Autor")
    categories = models.ManyToManyField(Category, verbose_name= "Categorias", related_name="get_posts")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "entrada"
        verbose_name_plural = "entradas"

    def __str__(self):
        return self.title
