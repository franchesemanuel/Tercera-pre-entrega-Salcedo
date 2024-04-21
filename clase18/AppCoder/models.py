from django.db import models

# Create your models here.siempre que creo un modelo nuevo debo hacer la migracion de nuevo !!!!

class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada=models.IntegerField()
    
    
