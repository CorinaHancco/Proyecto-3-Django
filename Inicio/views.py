from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def InicioDePagina(*args, **kwargs):
    return HttpResponse('<h1> Hola, tiene que registrarse </h1>')

def LoginVista (request,*args, **kwargs):
    return  render(request,"login.html",{})
