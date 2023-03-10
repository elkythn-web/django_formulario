from django.db import models

class Estudiante(models.Model):
    dni = models.CharField(max_length=15)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.CharField(max_length=15)
    CARRERA_CHOICES = (
        ('ingenieria', 'Ingeniería'),
        ('matematicas', 'Matemáticas'),
        ('fisica', 'Física'),
    )
    carrera = models.CharField(max_length=50, choices=CARRERA_CHOICES)

