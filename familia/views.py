from django.shortcuts import render
from familia.models import familia

def index(request):
    return render(request, "familia/familia.html")

###"""def saludar_a(requet):
   ### return render(request, "ejemplo/saludar_a.html)"""

def mostrar_familiar(request):
  lista_familiares = familia.objects.all()
  return render(request, "familia/familiar.html", {"lista_familiares": lista_familiares})

###def buscar(request):
### nombres=[ "Miguel", "Jose", "Enrique", "Santiago" ]
##  query = request.GET["q"]
### if query in nombres.
###  resultado=nombres.index(query)
###  indice= nombre.index(query) (parte 2)
### resultado = nombres[ indice ]
### else:
### resultado="no hay match"
###return render(request, "familia/buscar.html", {"resultado": resuiltado})