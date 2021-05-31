from django.db import models

# Create your models here.
class Estudiantes(models.Model):
    nombres = models.CharField(max_length=100) # es calmo es una caja de texto
    apellidos = models.CharField(max_length=100)    
    edad = models.IntegerField()
