from django.shortcuts import render
from django.views.generic import ListView
from django.http import JsonResponse
from administracion.models import Medico, Cita_medica
from django.db.models import Count

def inicio(request):
    lista_especialidades = Medico.objects.values('especialidad').annotate(Count('especialidad')).order_by('especialidad')
    return render(request, 'administracion/inicio.html', {'especialidades': lista_especialidades})

def listar_medicos(request, esp):
    lista_medicos = Medico.objects.all().filter(especialidad = esp)
    return render(request, 'administracion/medicos_especialidad.html', {'medicos': lista_medicos, 'especialidad': esp})

def fechas_disponibles(request):
    id_medico = request.GET.get('id', None)
    data = list(Cita_medica.objects.values('fecha_cita').annotate(Count('fecha_cita')).filter(medico = id_medico).order_by('fecha_cita'))
    return JsonResponse(data, safe=False)

def horas_disponibles(request):
    fecha_buscar = request.GET.get('fecha_buscar', None)
    id_medico = request.GET.get('id_medico', None)
    data = list(Cita_medica.objects.values('id', 'hora_inicio_cita', 'hora_fin_cita').filter(fecha_cita = fecha_buscar, medico = id_medico))
    return JsonResponse(data, safe=False)
