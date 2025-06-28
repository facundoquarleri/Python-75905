from django.urls import path

from . import views

app_name = "cliente"

urlpatterns = [
    path('', views.index, name='index'),
    path('cliente/list/', views.cliente_list, name = 'cliente_list'),
    path('pais/list/', views.pais_list, name= 'pais_list'),
]