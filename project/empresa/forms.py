from django import forms

from . import models

class EmpleadosCreateForm(forms.ModelForm):
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
