from django.shortcuts import render, redirect

from . import models, forms

def home (request):
    query = models.Areas.objects.all()
    contexto = {"areas": query}
    return render(request, "empresa/index.html", context=contexto)

def areas_create (request):
    if request.method == "POST":
        form = forms.AreasForm(request.POST)
        try:
            if form.is_valid:
                form.save()
                return redirect("empresa:home")
        except ValueError:
               ...
    else:  # request.method == "GET"
        form = forms.AreasForm()
    return render(request, "empresa/areas_create.html", context={"form": form})


def areas_detail(request, pk: int):
     query = models.Areas.objects.get(id=pk)
     return render(request, "empresa/areas_detail.html", {"area": query})

def areas_update(request, pk: int):
     query = models.Areas.objects.get(id=pk)
     if request.method == "POST":
         form = forms.AreasForm(request.POST, instance=query)
         if form.is_valid:
             form.save()
             return redirect("empresa:home")
     else:  # request.method == "GET"
         form = forms.AreasForm(instance=query)
     return render(request, "empresa/areas_update.html", context={"form": form , "query":query})

def areas_delete(request, pk: int):
    query = models.Areas.objects.get(id=pk)
    if request.method == "POST":
        query.delete()
        return redirect("empresa:home")
    return render(request, "empresa/areas_delete.html", context={"area": query})

def empleados(request):
    query = models.Empleados.objects.all()
    contexto = {"empleados": query}
    return render(request, "empresa/empleados.html", context=contexto)

def empleado_create (request):
    if request.method == "POST":
        form = forms.EmpleadosForm(request.POST)
        try:
            if form.is_valid:
                form.save()
                return redirect("empresa:empleados")
        except ValueError:
               ...
    else:  # request.method == "GET"
        form = forms.EmpleadosForm()
    return render(request, "empresa/empleado_create.html", context={"form": form})

def buscar_empleado(request):
    consulta = request.GET.get("consulta", None)
    if consulta:
        query = models.Empleados.objects.filter(documento__icontains=consulta)
        return render(request, "empresa/buscar_empleado.html", {"resultados": query})
    return render(request, "empresa/buscar_empleado.html")

def empleado_update(request, pk: int):
     query = models.Empleados.objects.get(id=pk)
     if request.method == "POST":
         form = forms.EmpleadosForm(request.POST, instance=query)
         if form.is_valid:
             form.save()
             return redirect("empresa:empleados")
     else:  # request.method == "GET"
         form = forms.EmpleadosForm(instance=query)
     return render(request, "empresa/empleado_update.html", context={"form": form})

def empleado_delete(request, pk: int):
    query = models.Empleados.objects.get(id=pk)
    if request.method == "POST":
        query.delete()
        return redirect("empresa:empleados")
    return render(request, "empresa/empleado_delete.html", context={"empleado": query})