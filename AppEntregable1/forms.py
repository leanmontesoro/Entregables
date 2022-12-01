from django import forms


class EquipoForm(forms.Form):
    nombre=forms.CharField(max_length=20)
    pais=forms.CharField(max_length=20)
    fec_fundacion=forms.DateField()

class JugadorForm(forms.Form):
    nombre=forms.CharField(max_length=20)
    apellido=forms.CharField(max_length=20)
    edad=forms.IntegerField()
    pais=forms.CharField(max_length=20)
    equipo=forms.CharField(max_length=20)
    posicion=forms.CharField(max_length=20)

class TecnicoForm(forms.Form):
    nombre=forms.CharField(max_length=20)
    apellido=forms.CharField(max_length=20)
    edad=forms.IntegerField()
    pais=forms.CharField(max_length=20)
    equipo=forms.CharField(max_length=20)    
