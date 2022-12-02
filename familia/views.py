from django.shortcuts import render
from familia.models import familia

def index(request):
    return render(request, "familia/familia.html")

def monstrar_familiar(request):
  lista_familiares = familia.objects.all()
  return render(request, "ejemplo/familiares.html", {"lista_familiares": lista_familiares})

  