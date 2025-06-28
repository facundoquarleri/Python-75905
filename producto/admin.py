from django.contrib import admin

# Register your models here.
from . import models

@admin.register(models.CategoriaProducto)
class ProductocategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion")
    search_fields = ("nombre",)