from django.db import models

# Create your models here.
## TODO: reformular models
class Familiar(models.Model):
    
    nombre=models.CharField(max_length=20,default="name")
    apellido=models.CharField(max_length=20,default="apellido")
    edad=models.IntegerField(default=0)
    fec_nac=models.DateField(default='2022-00-00')
    def __str__(self):
        return self.nombre
        #return self.nombre+" y mi edad es "+str(self.edad) +". Nací en " + str(self.fec_nac)

class Equipo(models.Model):
    
    nombre=models.CharField(max_length=20,default="name")
    pais=models.CharField(max_length=20,default="pais")
    fec_fundacion=models.DateField(default='2022-00-00')
    def __str__(self):
        return self.nombre


class Jugador(models.Model):
    
    nombre=models.CharField(max_length=20,default="name")
    apellido=models.CharField(max_length=20,default="apellido")
    edad=models.IntegerField(default=0)
    pais=models.CharField(max_length=20,default="pais")
    equipo=models.CharField(max_length=20,default="libre")
    posicion=models.CharField(max_length=20,default="libre")
    def __str__(self):
        return self.nombre + " " + self.apellido

class Tecnico(models.Model):
    
    nombre=models.CharField(max_length=20,default="name")
    apellido=models.CharField(max_length=20,default="apellido")
    edad=models.IntegerField(default=0)
    pais=models.CharField(max_length=20,default="pais")
    equipo=models.CharField(max_length=20,default="libre")
    
    def __str__(self):
        return self.nombre + " " + self.apellido