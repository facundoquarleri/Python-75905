from django import forms

from . import models

class ProductoCategoriaForm(forms.ModelForm):
    class Meta:
        model = models.CategoriaProducto
        fields = "__all__"