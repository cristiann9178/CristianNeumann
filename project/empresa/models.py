from django.db import models

class Empleados(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField(max_length=3)
    email = models.EmailField(max_length=50)

    def __str__(self) -> str:
        return self.nombre
    
class Cargo(models.Model):
    nombre = models.CharField(max_length=100)
    empleado = models.ForeignKey(Empleados, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.nombre

class Areas(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    ubicacion = models.CharField(max_length=100)
    empleados = models.ForeignKey(Empleados, on_delete=models.SET_NULL)  