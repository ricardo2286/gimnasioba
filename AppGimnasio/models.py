from django.db import models

# Create your models here.
class musculacion(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    

class yoga(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    pago = models.BooleanField()    

class natacion(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    pago = models.BooleanField()    