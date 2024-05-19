from django.contrib import admin

from . import models

class CargoAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "salario"
    )

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "apellido",
        "email",
        "cargo",
    )
    search_fields = ("nombre",)
    ordering = ("nombre",)

class AreasAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "ubicacion",
    )


admin.site.register(models.Areas, AreasAdmin)
admin.site.register(models.Empleados, EmpleadoAdmin)
admin.site.register(models.Cargo, CargoAdmin)