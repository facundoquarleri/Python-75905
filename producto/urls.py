from django.urls import path

from . import views

app_name = "producto"

urlpatterns = [
    path('', views.index, name="index"),
    path('productocategoria/list/',
        views.ProductoCategoriaListViews.as_view(),
        name = "productocategoria_list"
        ),
    path('productocategoria/create/',
        views.ProductoCategoriaCreateView.as_view(),
        name= "productocategoria_create"
        ),
    path('productocategoria/<int:pk>/',
        views.ProductoCategoriaDetailView.as_view(),
        name="productocategoria_detail"
        ),
    path('productocategoria/<int:pk>/update/',
        views.ProductoCategoriaUpdateView.as_view(),
        name="productocategoria_update"
        ),
    path('productocategoria/<int:pk>/delete/',
        views.ProductoCategoriaDeleteView.as_view(),
        name="productocategoria_delete"
        ),
]