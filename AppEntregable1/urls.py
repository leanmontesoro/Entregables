from django.urls import path
from AppEntregable1.views import *


urlpatterns = [

        path('familia/', Familia, name= "flia"),

]