import datetime
import secrets
from django.contrib.auth.hashers import make_password, identify_hasher
from django.db import models


# Create your models here.
class Ramo(models.Model):
    ramoId=models.BigAutoField(primary_key=True)
    ramoLetra=models.CharField(max_length=4)
    ramoNum=models.IntegerField()
    ramoNombre=models.CharField(max_length=100)

class Profesor(models.Model):
    profeId=models.BigAutoField(primary_key=True)
    profeMail=models.CharField(max_length=100)
    profeUser=models.CharField(max_length=40)
    profePass=models.CharField(max_length=3000) 

    def save(self,*args,**kwargs):
        try:
            identify_hasher(self.profePass)
        except:
            self.profePass=make_password(self.profePass)
        super(Profesor,self).save(*args,**kwargs)

class Seccion(models.Model):
    seccionId=models.BigAutoField(primary_key=True)
    seccionNum=models.IntegerField()
    seccionTipo=models.CharField(max_length=1,choices=(('D','Diurno'),('V','Vespertino')))
    seccionRamo=models.ForeignKey(Ramo, on_delete=models.CASCADE)
    seccionProfesor=models.ForeignKey(Profesor, on_delete=models.CASCADE)

class Alumno(models.Model):
    alumnoId=models.BigAutoField(primary_key=True)
    alumnoRut=models.IntegerField(unique=True)
    alumnoDv=models.CharField(max_length=1)
    alumnoNombre=models.CharField(max_length=200)
    alumnoUser=models.CharField(max_length=40)
    alumnoPass=models.CharField(max_length=3000)

    def save(self,*args,**kwargs):
        try:
            identify_hasher(self.alumnoPass)
        except ValueError:
            self.alumnoPass=make_password(self.alumnoPass)
        super(Alumno,self).save(*args,**kwargs)

class Clase(models.Model):
    claseId=models.BigAutoField(primary_key=True)
    claseDate=models.DateTimeField(default=datetime.datetime.now)
    claseProfe=models.ForeignKey(Profesor, on_delete=models.CASCADE)
    claseSeccion=models.ForeignKey(Seccion,on_delete=models.CASCADE)

class Asistencia(models.Model):
    asistenciaId=models.BigAutoField(primary_key=True)
    asistenciaAlumno=models.ForeignKey(Alumno, on_delete=models.CASCADE)
    asistenciaClase=models.ForeignKey(Clase, on_delete=models.CASCADE)
    presente=models.BooleanField(default=False)

class CodigoQR(models.Model):
    codigoId=models.BigAutoField(primary_key=True)
    codigo=models.CharField(max_length=500, blank=True, null=True)
    fechaexp=models.DateTimeField(blank=True, null=True)
    codigoClase=models.ForeignKey(Clase,on_delete=models.CASCADE)
    def save(self,*args,**kwargs):
        self.codigo=secrets.token_urlsafe(50)
        self.fechaexp=datetime.datetime.now() + datetime.timedelta(minutes=30)
        super(CodigoQR,self).save(*args,**kwargs)
