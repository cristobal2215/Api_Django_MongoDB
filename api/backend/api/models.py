from django.db import models

# Create your models here.
class Estudiante(models.Model):
    Nombre=models.CharField(max_length=100)
    Apellido=models.CharField(max_length=100)
    Edad=models.PositiveIntegerField()
    Ramo=models.CharField(max_length=100)
    Profesor=models.CharField(max_length=100)
    
