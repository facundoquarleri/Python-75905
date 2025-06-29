from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
# Create your views here.
from . import models, forms
def index(request):
    return render(request, 'producto/index.html')

#def productocategoria_list(request):
#    productocategoria = models.CategoriaProducto.objects.all()
#    contexto = {"productocategoria": productocategoria}
#    return render(request, 'producto/productocategoria_list.html', contexto)
class ProductoCategoriaListViews(ListView):
    model = models.ProductoCategoria
#    context_object_name = "productocategoria"



#def productocategoria_create(request):
#    if request.method == "GET":
#        formulario = forms.ProductoCategoriaForm()
#    if request.method == "POST":
#        form = forms.ProductoCategoriaForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect("producto:productocategoria_list")
#    
#    contexto = {"formulario" : formulario}
#    return render(request, 'producto/productocategoria_create.html', contexto)

class ProductoCategoriaCreateView(CreateView):
    model = models.ProductoCategoria
    form_class = forms.ProductoCategoriaForm
    success_url = reverse_lazy("producto:productocategoria_list")
    template_name = "producto/productocategoria_create.html"

class ProductoCategoriaDetailView(DetailView):
    model = models.ProductoCategoria
    template_name = "producto/productodetalle.html"

class ProductoCategoriaUpdateView(UpdateView):
    model = models.ProductoCategoria
    form_class = forms.ProductoCategoriaForm
    success_url = reverse_lazy("producto:productocategoria_list")
    template_name = "producto/productoeditar.html"

class ProductoCategoriaDeleteView(DeleteView):
    model = models.ProductoCategoria
    success_url = reverse_lazy("producto:productocategoria_list")
    template_name = "producto/productoeliminar.html"