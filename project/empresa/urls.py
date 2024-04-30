from django.urls import path
from . import views

app_name = "empresa"

urlpatterns = [
    path('', views.home, name="home"),
    path('empleados/create/', views.empleado_create, name="empleado_create"),
    path('empleados/', views.empleados, name="empleados"),
    path('empleados/buscar/', views.buscar_empleado, name="buscar_empleados"),
]