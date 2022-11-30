from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Familiar
# Create your views here.


def inicio(request):
    #mensaje={"mensaje":"Soy la pagina de inicio"}
    #plantilla= loader.get_template("template_inicio.html")
    #documento=plantilla.render(mensaje)
    #return HttpResponse(documento)
    return render (request, "../../AppEntregable1/templates/template_padre.html")


def familia(request):

#Creo objetos Familiar y los guardo.
    hermano=Familiar(nombre="Leandro",apellido="Montesoro",edad=19,fec_nac="2022-01-03")
    hermano.save()
    padre=Familiar(nombre="Carlos",apellido="Montesoro",edad=55,fec_nac="2022-01-03")
    padre.save()
    madre=Familiar(nombre="Norma",apellido="Montesoro",edad=65,fec_nac="2022-01-03")
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
        "ap_hermano":hermano.apellido,
        
        
        "nom_padre":padre.nombre,
        "edad_padre":padre.edad,
        "fec_nac_padre":padre.fec_nac,
        "ap_padre":padre.apellido,

        "nom_madre":madre.nombre,
        "edad_madre":madre.edad,
        "fec_nac_madre":madre.fec_nac,
        "ap_madre":madre.apellido
    }

    #plantilla= loader.get_template("template.html")
    #documento=plantilla.render(diccionario_fliar)
    #return HttpResponse(documento)
    return render (request, "../../AppEntregable1/templates/familia.html",diccionario_fliar)



def madres(request):

    return render (request, "../../AppEntregable1/templates/madres.html")

def padres(request):
    
    return render (request, "../../AppEntregable1/templates/padres.html")


def hermanos(request):
    
    return render (request, "../../AppEntregable1/templates/hermanos.html")

def familiaFormulario(request):

    if request.method=="POST":
        name=request.POST["nombre"]
        address=request.POST["apellido"]    
        age=request.POST["edad"]
        date=request.POST["fec_nac"]

        familiar1=Familiar(nombre=name,apellido=address,edad=age,fec_nac=date)
        familiar1.save()
        ##guardo y mando a inicio
        return render (request, "../../AppEntregable1/templates/template_padre.html")

    return render(request, "../../AppEntregable1/templates/familiaFormulario.html")

#     <p> Nombre:          <input type="text" name="nombre">    </p>
# <p> Apellido:          <input type="text" name="apellido">    </p>
# <p> Edad:          <input type="text" name="edad">    </p>
# <p> Fecha de nacimiento:          <input type="text" name="fec_nac">    </p>