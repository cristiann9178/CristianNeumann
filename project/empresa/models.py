from django.db import models

class Cargo(models.Model):
    nombre = models.CharField(max_length=100)
    salario = models.PositiveIntegerField(default=0, null=False)
                                              
    def __str__(self):
        return self.nombre

    
class Empleados(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.PositiveIntegerField(default=0, null=False)
    email = models.EmailField(max_length=50)
    #area = models.ForeignKey(Areas, on_delete=models.SET_NULL, null=True, blank=True)
    cargo = models.ForeignKey(Cargo, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name_plural = "empleados"

    def __str__(self) -> str:
        return self.nombre
     
class Areas(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="área")
    descripcion = models.CharField(max_length=200)
    ubicacion = models.CharField(max_length=100)
    empleados = models.ManyToManyField(Empleados, null=True, blank=True, limit_choices_to={'areas__isnull':True})

    class Meta:
        verbose_name_plural = "áreas"
    
    def __str__(self) -> str:
        return self.nombre