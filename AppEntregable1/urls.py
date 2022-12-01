from django.urls import path
from AppEntregable1.views import *


urlpatterns = [

        
        path('equipo/', equipo, name= "equipo"),
        path('jugador/', jugador, name= "jugador"),
        path('tecnico/', tecnico, name= "tecnico"),
        path('jugadorFormulario/',jugadorFormulario, name="jugadorFormulario"),
        path('tecnicoFormulario/',tecnicoFormulario, name="tecnicoFormulario"),
        path('equipoFormulario/',equipoFormulario, name="equipoFormulario"),
        path("busquedaJugador/", busquedaJugador, name="busquedaJugador"),
        path("buscar/", buscar, name="buscar"),

]