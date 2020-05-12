from django.shortcuts import render
from django.http import JsonResponse
from administracion.models import Medico
from django.db.models import Count

def inicio(request):
    lista_especialidades = Medico.objects.values('especialidad').annotate(Count('especialidad')).order_by('especialidad')
    return render(request, 'administracion/inicio.html', {'especialidades': lista_especialidades})

def listar_medicos(request, esp):
    lista_medicos = Medico.objects.values('nombre', 'apellidos', 'especialidad', 'id', 'genero', 'foto_perfil').filter(especialidad = esp)
    return render(request, 'administracion/medicos_especialidad.html', {'medicos': lista_medicos, 'especialidad': esp})
