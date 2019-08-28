from django.db import models
from datetime import datetime,date

class Pacientes(models.Model):
    tipo_documento = models.CharField(max_length=3, choices=[
        ('DNI', 'DNI'),
        ('CE', 'Carné de Extranjería'),
        ('IN', 'Indocumentado'),
    ], default='DNI')
    numero_documento = models.CharField(max_length=100, unique=True)
    nombres = models.TextField()
    appPaterno = models.CharField(max_length=100)
    appMaterno = models.CharField(max_length=100)
    fecha = models.DateField()
