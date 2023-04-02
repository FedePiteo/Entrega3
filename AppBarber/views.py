from django.shortcuts import render
from AppBarber.models import Turno, Cliente, Barbero
from django.http import HttpResponse
from django.shortcuts import render

def sacar_turno(request):
    return render(request, "AppBarber/sacar_turno.html")