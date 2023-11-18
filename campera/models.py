from django.db import models

class Campera(models.Model):
    talle = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=250)
    fecha_creacion = models.DateField()
    
    def __str__(self):
        return f'{self.talle} - {self.color}'

class Remera(models.Model):
    estilo = models.CharField(max_length=30)
    talle = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    fecha_creacion = models.DateField()
    
    def __str__(self):
        return f'{self.estilo} - {self.talle}'