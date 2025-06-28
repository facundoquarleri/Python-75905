from django.shortcuts import render

# Create your views here.
from . import models    
def index(request):
    return render(request, 'producto/index.html')

def productocategoria_list(request):
    productocategoria = models.CategoriaProducto.objects.all()
    contexto = {"productocategoria": productocategoria}
    return render(request, 'producto/productocategoria.html', contexto)