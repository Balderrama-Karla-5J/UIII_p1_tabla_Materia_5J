from django.shortcuts import render,redirect
from .models import materia

# Create your views here.
def inicio_vista(request):
    lasmaterias=materia.objects.all()
    return render (request,"gestionarmnateria.html", {"mismaterias":lasmaterias})

def registrarMateria(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    creditos=request.POST["numcreditos"]

    guardarmateria=materia.objects.create(
        codigo=codigo,nombre=nombre,creditos=creditos
    ) # GUARDA EL REGISTRO

    return redirect("/")