from django.urls import path
from . import views

app_name = "empresa"

urlpatterns = [
    path('', views.home, name="home"),
    path('empleados/create/', views.empleado_create, name="empleado_create"),
]