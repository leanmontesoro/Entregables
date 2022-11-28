from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import GrupoFamiliar
# Create your views here.


def inicio(request):
    #mensaje={"mensaje":"Soy la pagina de inicio"}
    #plantilla= loader.get_template("template_inicio.html")
    #documento=plantilla.render(mensaje)
    #return HttpResponse(documento)
    return render (request, "../../AppEntregable1/templates/template_inicio.html",{"mensaje":"Soy la pagina de inicio"})


def Familia(request):

#Creo objetos GrupoFamiliar y los guardo.
    hermano=GrupoFamiliar(nombre="Leandro",edad=19,fec_nac="2022-01-03",apellido="monte")
    hermano.save()
    padre=GrupoFamiliar(nombre="Carlos",edad=55,fec_nac="2022-01-03",apellido="monte")
    padre.save()
    madre=GrupoFamiliar(nombre="Norma",edad=65,fec_nac="2022-01-03",apellido="monte")
    madre.save()

#Creo diccionario con objetos
    diccionario_fliar={

        #pasar objeto solo?
        # hermano,
        # padre,
        # madre
        "nom_hermano":hermano.nombre,
        "edad_hermano":hermano.edad,
        "fec_nac_hermano":hermano.fec_nac,
        
        "nom_padre":padre.nombre,
        "edad_padre":padre.edad,
        "fec_nac_padre":padre.fec_nac,

        "nom_madre":madre.nombre,
        "edad_madre":madre.edad,
        "fec_nac_madre":madre.fec_nac
    }

    plantilla= loader.get_template("template.html")
    documento=plantilla.render(diccionario_fliar)

   
    return HttpResponse(documento)