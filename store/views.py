from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("¡Bienvenido a la tienda en linea!")

def about(request):
    return HttpResponse("Acerca de Nosotros")

