from django import forms

from . import models

class EmpleadosForm(forms.ModelForm):
    class Meta:
        model = models.Empleados
        fields = "__all__"
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "apellido": forms.TextInput(attrs={"class": "form-control"}),
            "edad": forms.NumberInput(attrs={"class": "form-control"}),
            "documento": forms.NumberInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "cargo": forms.Select(attrs={"class": "form-control"}),
        }

class AreasForm(forms.ModelForm):
    class Meta:
        model = models.Areas
        fields = "__all__"
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "descripcion": forms.TextInput(attrs={"class": "form-control"}),
            "ubicacion": forms.TextInput(attrs={"class": "form-control"}),
            "empleados": forms.SelectMultiple(attrs={"class": "form-control"}),
        }