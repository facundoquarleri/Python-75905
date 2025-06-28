from django.db import models

class Pais(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.nombre}"
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    mail = models.EmailField(max_length=50)
    nacimiento = models.DateField(null=True, blank=True)
    pais_origen = models.ForeignKey(
        Pais, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return f"{self.apellido.capitalize()} {self.nombre.capitalize()}"

"""
pais = Pais(nombre = "Uruguay")
pais.save()
from datetime import date
persona =  Cliente(nombre = "Marco", apellido= Lopez, nacimiento = date(2005,1,1), pais_origen = 1)"""
