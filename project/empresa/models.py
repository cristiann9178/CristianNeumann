from django.db import models

class Cargo(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    salario = models.PositiveIntegerField(default=0)
                                              
    def __str__(self):
        return self.nombre

    
class Empleados(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.PositiveIntegerField(default=0, null=False)
    documento = models.PositiveIntegerField(default=0, null=False)
    email = models.EmailField(max_length=50, unique=True)
    cargo = models.ForeignKey(Cargo, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name="empleado"
        verbose_name_plural = "empleados"

    def __str__(self) -> str:
        return f"{self.nombre}" + f" {self.apellido}"
     
class Areas(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.CharField(max_length=200)
    ubicacion = models.CharField(max_length=100)
    empleados = models.ManyToManyField(Empleados, null=True, blank=True)

    class Meta:
        verbose_name="área"
        verbose_name_plural = "áreas"
    
    def __str__(self) -> str:
        return self.nombre