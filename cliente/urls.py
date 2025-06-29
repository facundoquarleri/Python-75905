from django.urls import path

from . import views

app_name = "cliente"

urlpatterns = [
    path('', views.index, name='index'),
    path('cliente/list/', views.cliente_list, name = 'cliente_list'),
    path('cliente/list/admin/', views.cliente_list_admin, name = 'cliente_list_admin'),
    path('cliente/login/', views.cliente_login, name = 'cliente_login'),
    path('pais/list/', views.pais_list, name= 'pais_list'),
    path('cliente/datos/', views.clientedatos, name='clientedatos'),
    path('admin/login/', views.admin_login, name='admin_login'),
    path('cliente/<int:pk>/', views.ClienteDetailView.as_view(), name='clientedetail'),
]