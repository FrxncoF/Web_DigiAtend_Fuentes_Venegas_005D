from django.shortcuts import render
from django.http import JsonResponse
from core.models import *

# Create your views here.

def generar_codigo(request, clase):
    codigo = CodigoQR(codigoClase = Clase.objects.get(pk = clase))
    codigo.save()
    json = {
    'codigo': codigo.codigo
    }
    return JsonResponse(json)