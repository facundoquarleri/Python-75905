from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    mail = models.EmailField(max_length=50)

    def __str__(self):
        return f"{self.apellido.capitalize()} {self.nombre.capitalize()}"
