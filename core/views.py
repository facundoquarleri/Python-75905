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

def ejercicio(request):
    nombre = "Louis"
    apellido = "Beethoven" 
    return render(request, 'core/ejercicio.html', {"nombre": nombre, "apellido": apellido})

def ejercicio2(request):
    datos = [
        {"nombre" : "Facu", "mail" : "facu@123"},
        {"nombre" : "Matias", "mail" : "mati@123"}
            ]

    return render (request, 'core/ejercicio2.html', {"usuarios": datos})
