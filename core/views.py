from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render (request, 'core/index.html')

def saludar(request):
    return HttpResponse ("Hola")

def saludar_parametros(request, nombre:str, apellido:str):
    nombre = nombre.capitalize()
    apellido = apellido.capitalize()
    return HttpResponse(f"Bienvenido {nombre} {apellido}")  

