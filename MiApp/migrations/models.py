from django.db import models

# Create your models here.

class Clase1(models.Model):
    campo1=models.CharField(max_length=50)

#Defino más campos

class Clase2(models.Model): 
     campo2 = models.IntegerField()

class Clase3(models.Model): 
     campo3 = models.DateFieldField()   