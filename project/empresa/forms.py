from django import forms

from . import models

class EmpleadosCreateForm(forms.ModelForm):
    class Meta:
        model = models.Empleados
        fields = "__all__"
        #widgets = {
        #    "nombre": forms.TextInput(attrs={"class": "form-control"}),
        #    "descripcion": forms.TextInput(attrs={"class": "form-control"}),
            #"edad": forms.TextInput(attrs={"class": "form-control"}),
            #"email": forms.TextInput(attrs={"class": "form-control"}),
            #"cargo": forms.TextInput(attrs={"class": "form-control"}),
        #}
