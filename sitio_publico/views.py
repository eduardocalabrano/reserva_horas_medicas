from django.shortcuts import render
from django.http import JsonResponse
from administracion.models import Medico

def inicio(request):
    lista_especialidades = Medico.objects.all()
    return render(request, 'administracion/inicio.html', {'especialidades': lista_especialidades})

def listar_medicos(request, esp):
    return render(request, 'administracion/medicos_especialidad.html', {})

