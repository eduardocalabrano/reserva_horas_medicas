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

def horas_disponibles(request):
    id_medico = request.GET.get('id', None)
    horariosdisponibles = Cita_medica.objects.all().filter(medico = id_medico)
    # data = []
    # for x in horariosdisponibles:
    #     # datos_horario = {
    #     #     'fecha' : x['fecha_cita'],
    #     #     'inicio' : x['hora_inicio_cita'],
    #     #     'fin' : x['hora_fin_cita'],
    #     # }
    #     datos_horario = {
    #         'numero' : x
    #     }
    #     data.append(datos_horario)
    # EN VEZ DE RETORNAR UN JSON PUEDO RETORNAR TODA LA INFORMACION NECESARIA PARA EL SELECT DE FECHAS
    data = [{'nombre': 'Alonso'},{'nombre': 'Juan'}] #Solo de ejemplo
    return JsonResponse(data, safe=False)
