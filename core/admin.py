from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Ramo)
admin.site.register(Profesor)
admin.site.register(Seccion)
admin.site.register(Alumno)
admin.site.register(Clase)
admin.site.register(Asistencia)
admin.site.register(CodigoQR)

