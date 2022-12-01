from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import *
from AppEntregable1.forms import *
# Create your views here.

## VISTAS
def inicio(request):
    return render (request, "../../AppEntregable1/templates/template_inicio.html",{"mensaje1":"Bienvenido!","mensaje2":"URL's disponibles:"})

def equipo(request):

    return render (request, "../../AppEntregable1/templates/equipo.html")

def jugador(request):
    
    return render (request, "../../AppEntregable1/templates/jugador.html")


def tecnico(request):
    
    return render (request, "../../AppEntregable1/templates/tecnico.html")

## FORMULARIOS

def jugadorFormulario(request):

    if request.method=="POST":
        form=JugadorForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            name=informacion["nombre"]
            address=informacion["apellido"]    
            age=informacion["edad"]
            country=informacion["pais"]
            team=informacion["equipo"]
            position=informacion["posicion"]

            jugador1=Jugador(nombre=name,apellido=address,edad=age,pais=country,equipo=team,posicion=position)
            jugador1.save()
            ##guardo y mando a inicio
            return render (request, "../../AppEntregable1/templates/template_inicio.html")
    else:
        formulario=JugadorForm()

    return render (request, "../../AppEntregable1/templates/jugadorFormulario.html",{"form":formulario})

def tecnicoFormulario(request):
    if request.method=="POST":
        form=TecnicoForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            name=informacion["nombre"]
            address=informacion["apellido"]    
            age=informacion["edad"]
            country=informacion["pais"]
            team=informacion["equipo"]
            

            tecnico1=Tecnico(nombre=name,apellido=address,edad=age,pais=country,equipo=team)
            tecnico1.save()
            ##guardo y mando a inicio
            return render (request, "../../AppEntregable1/templates/template_inicio.html")
    else:
        formulario=JugadorForm()
    return render(request, "../../AppEntregable1/templates/tecnicoFormulario.html",{"form":formulario})

def equipoFormulario(request):

    if request.method=="POST":
        form=EquipoForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            name=informacion["nombre"]
            country=informacion["pais"]
            date=informacion["fec_fundacion"]
        

        equipo1=Equipo(nombre=name,pais=country,fec_fundacion=date)
        equipo1.save()
        ##guardo y mando a inicio
        return render (request, "../../AppEntregable1/templates/template_inicio.html")
    else:
        formulario=EquipoForm()
    return render(request, "../../AppEntregable1/templates/equipoFormulario.html",{"form":formulario})


## BUSQUEDAS

def busquedaJugador(request):
    return render(request, "../../AppEntregable1/templates/busquedaJugador.html")

def buscar(request):

    if request.GET["equipo"]:

        equipo=request.GET["equipo"]

        jugadores=Jugador.objects.filter(equipo__icontains=equipo)
        return render(request,"../../AppEntregable1/templates/resultadoBusquedaJugador.html", {"jugadores":jugadores} )
    else:
        return render(request, "../../AppEntregable1/templates/busquedaJugador.html", {"mensaje":"Debe ingresar un equipo"})