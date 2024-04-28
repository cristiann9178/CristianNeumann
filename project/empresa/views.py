from django.shortcuts import render, redirect

from . import models, forms

def home (request):
    query = models.Areas.objects.all()
    contexto = {"areas": query}
    return render(request, "empresa/index.html", context=contexto)

def empleado_create (request):
    if request.method == "POST":
        form = forms.EmpleadosCreateForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("empresa:home")
    else:  # request.method == "GET"
        form = forms.EmpleadosCreateForm()
    return render(request, "empresa/empleado_create.html", context={"form": form})
    #return render (request, "empresa/empleado_create.html")