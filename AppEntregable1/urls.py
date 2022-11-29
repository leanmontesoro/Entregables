from django.urls import path
from AppEntregable1.views import *


urlpatterns = [

        path('familia/', familia, name= "flia"),
        path('padres', padres, name= "padres"),
        path('madres', madres, name= "madres"),
        path('hermanos', hermanos, name= "hermanos"),
        path('familiaFormulario/',familiaFormulario, name="familiaFormulario"),

]