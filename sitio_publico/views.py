from django.shortcuts import render
from django.views.generic import ListView
from django.http import JsonResponse
from administracion.models import Medico, Cita_medica, Paciente
from django.db.models import Count
from django.utils import timezone, dateformat
# from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.template.loader import render_to_string

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
    id_medico = request.GET.get('id_medico', None)

    fecha_buscar = request.GET.get('fecha_buscar', None)
    hoy = dateformat.format(timezone.localtime(timezone.now()), 'Y-m-d')

    if(fecha_buscar == hoy):
        now = timezone.localtime(timezone.now())  + timezone.timedelta(minutes=29) #se obtiene la hora de la fecha actual
        data = list(Cita_medica.objects.values('id', 'hora_inicio_cita', 'hora_fin_cita').filter(fecha_cita = fecha_buscar, medico = id_medico, hora_inicio_cita__gte = now.time(), estado_cita = 'DIS').order_by('hora_inicio_cita'))
    else:
        data = list(Cita_medica.objects.values('id', 'hora_inicio_cita', 'hora_fin_cita').filter(fecha_cita = fecha_buscar, medico = id_medico, estado_cita = 'DIS').order_by('hora_inicio_cita'))
    return JsonResponse(data, safe=False)

def ingresa_paciente(request):
    id_hora = request.GET.get('id_hora', None)
    rut_paciente = request.GET.get('rut', None)
    nom_paciente = request.GET.get('nom', None)
    ape_paciente = request.GET.get('ape', None)
    fon_paciente = request.GET.get('fon', None)
    ema_paciente = request.GET.get('ema', None)
    now = timezone.localtime(timezone.now())
    # data_paciente = Paciente.objects.values('id').filter(rut=rut_paciente).first()
    try:
        data_paciente = Paciente.objects.get(rut=rut_paciente) #al usar get si no hay resultado se retorna un DoesNotExist
    except Paciente.DoesNotExist:
        data_paciente = None
    if not data_paciente:
        '''
        Paciente no existe previamente en la base de datos, debe crearse como primer paso.
        '''
        nuevo_paciente = Paciente(rut=rut_paciente, nombre=nom_paciente, apellidos=ape_paciente, telefono=fon_paciente, email=ema_paciente)
        nuevo_paciente.save()
        obj = Cita_medica.objects.get(id=id_hora)
        obj.paciente = nuevo_paciente
        obj.estado_cita = 'RES'
        obj.fecha_actualizacion = now
        medico_data = obj.medico
        fecha_data = obj.fecha_cita
        hora_data = obj.hora_inicio_cita
        obj.save()
        data = {
            'respuesta': 'paciente y reserva creados exitosamente',
        }
        html_message = render_to_string('administracion/mail_template.html', {'paciente_nombre': nom_paciente, 'paciente_apellido': ape_paciente, 'med_data': medico_data, 'fecha': fecha_data, 'hora': hora_data})
        mensaje = ''
        send_mail('Aviso de reserva de hora médica',mensaje,'ecalabra.dev@gmail.com',[ema_paciente],fail_silently=False, html_message=html_message)
    else:
        obj = Cita_medica.objects.get(id=id_hora)
        obj.paciente = data_paciente
        obj.estado_cita = 'RES'
        obj.fecha_actualizacion = now
        obj.save()
        data = {
            'respuesta': 'reserva realizada',
        }
        html_message = render_to_string('administracion/mail_template.html', {'paciente_nombre': nom_paciente, 'paciente_apellido': ape_paciente})
        mensaje = ''
        send_mail('Aviso de reserva de hora médica',mensaje,'ecalabra.dev@gmail.com',[ema_paciente],fail_silently=False, html_message=html_message)
    return JsonResponse(data, safe=False)
