from django.db import models

# Create your models here.
class CategoriaProducto(models.Model):

    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre
    

class Meta(models.Model):
    verbose_name = "Categoria de Producto"
    verbose_name_plural = "Categorias de productos"