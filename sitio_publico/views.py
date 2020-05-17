from django.shortcuts import render
from django.views.generic import ListView
from django.http import JsonResponse
from administracion.models import Medico, Cita_medica, Paciente
from django.db.models import Count
from django.utils import timezone

def inicio(request):
    lista_especialidades = Medico.objects.values('especialidad').annotate(Count('especialidad')).order_by('especialidad')
    return render(request, 'administracion/inicio.html', {'especialidades': lista_especialidades})

def listar_medicos(request, esp):
    lista_medicos = Medico.objects.all().filter(especialidad = esp)
    return render(request, 'administracion/medicos_especialidad.html', {'medicos': lista_medicos, 'especialidad': esp})

def fechas_disponibles(request):
    '''
    vista que retorna a la llamada ajax el listado de fechas disponibles para el médico.
    La fecha disponible no puede ser inferior a la del día en curso.
    '''
    now = timezone.localtime(timezone.now()) #timezone.now() devuelve la fecha para formato UTC, al transformar a localtime se pasa al formato ingresado en settings.
    id_medico = request.GET.get('id', None)
    data = list(Cita_medica.objects.values('fecha_cita').annotate(Count('fecha_cita')).filter(medico = id_medico, fecha_cita__gte = now).order_by('fecha_cita'))
    return JsonResponse(data, safe=False)

def horas_disponibles(request):
    '''
    vista que retorna a la llamada ajax el listado de horarios disponibles para la fecha y médico en consulta.
    Los horarios no pueden ser inferior a la hora en curso y muestra solo horarios con hora de inicio minimo 29 minutos
    despues del horario en que se consulta.
    '''
    now = timezone.localtime(timezone.now())  + timezone.timedelta(minutes=29) #se obtiene la hora de la fecha actual
    fecha_buscar = request.GET.get('fecha_buscar', None)
    id_medico = request.GET.get('id_medico', None)
    data = list(Cita_medica.objects.values('id', 'hora_inicio_cita', 'hora_fin_cita').filter(fecha_cita = fecha_buscar, medico = id_medico, hora_inicio_cita__gte = now.time()).order_by('hora_inicio_cita'))
    return JsonResponse(data, safe=False)

def ingresa_paciente(request):
    id_hora = request.GET.get('id_hora', None)
    rut_paciente = request.GET.get('rut', None)
    nom_paciente = request.GET.get('nom', None)
    ape_paciente = request.GET.get('ape', None)
    fon_paciente = request.GET.get('fon', None)
    ema_paciente = request.GET.get('ema', None)
    data_paciente = Paciente.objects.all().filter(rut=rut_paciente)
    if not data_paciente:
        # objects.create no sirve para la vista. Es necesario investigar más sobre como instanciar un modelo en la vista.
        # https://docs.djangoproject.com/en/3.0/ref/models/instances/
        data = {
            'respuesta': 'sin datos para el rut',
            'rut':rut_paciente,
        }
    else:
        data = {
            'respuesta': 'paciente ya existe en BD',
            'rut':rut_paciente,
        }
    return JsonResponse(data, safe=False)
