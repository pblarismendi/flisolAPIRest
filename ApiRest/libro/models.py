from django.db import models

# Create your models here.
class Libro(models.Model):
    titulo = models.CharField(max_length=50, default='')
    autor = models.CharField(max_length=50, default='')
    edicion = models.IntegerField()
