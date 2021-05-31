from django.db import models

# Create your models here.
class Estudinates(models.Model):
    nombres = models.TextField() # es calmo es una caja de texto
    apellidos = models.TextField()
    edad = models.TextField()
