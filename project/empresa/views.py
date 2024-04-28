from django.shortcuts import render

from . import models

def home (request):
    query = models.Areas.objects.all()
    contexto = {"areas": query}
    return render(request, "empresa/index.html", context=contexto)