from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.hashers import make_password, identify_hasher, check_password
from .models import *

# Create your views here.

def register(request):
    return render(request,'core/register.html')

def login(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        email = request.POST['email']
        password = request.POST['password']
        profe = Profesor(profeUser = nombre, profeMail = email, profePass = password)
        profe.save()
        return HttpResponseRedirect('/')
    else:
        return render(request, 'core/login.html')

def qrcode(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        password = request.POST['password']
        print(nombre,password)
        if Profesor.objects.filter(profeUser = nombre).exists():
            profe = Profesor.objects.get(profeUser = nombre)
            if check_password(password, profe.profePass):
                request.session['user'] = nombre
                return HttpResponseRedirect('/qrcode')
            else:
                return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/')
    else:
        profe = Profesor.objects.get(profeUser = request.session['user'])
        clases = Clase.objects.filter(claseProfe = profe).all()
        return render(request, 'core/qrcode.html',{'clases': clases})