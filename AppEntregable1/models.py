from django.db import models

# Create your models here.

class GrupoFamiliar(models.Model):
    
    nombre=models.CharField(max_length=20,default="name")
    apellido=models.CharField(max_length=20,default="apellido")
    edad=models.IntegerField(default=0)
    fec_nac=models.DateField(default='2022-00-00')


    def __str__(self):
        return self.nombre
        #return self.nombre+" y mi edad es "+str(self.edad) +". Nací en " + str(self.fec_nac)