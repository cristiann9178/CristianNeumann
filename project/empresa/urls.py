from django.urls import path
from . import views

app_name = "empresa"

urlpatterns = [
    path('', views.home, name="home"),
    path('empleados/create/', views.empleado_create, name="empleado_create"),
    path('empleados/', views.empleados, name="empleados"),
    path('empleados/buscar/', views.buscar_empleado, name="buscar_empleados"),
    path('empleados/update/<int:pk>', views.empleado_update, name="empleado_update"),
    path('empleados/delete/<int:pk>', views.empleado_delete, name="empleado_delete"),
    path('areas/create/', views.areas_create, name="areas_create"),
    path('areas/detail/<int:pk>', views.areas_detail, name="areas_detail"),
    path('areas/update/<int:pk>', views.areas_update, name="areas_update"),
    path('areas/delete/<int:pk>', views.areas_delete, name="areas_delete"),
]