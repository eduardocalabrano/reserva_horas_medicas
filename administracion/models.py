from django.db import models
from django.utils import timezone

class Persona(models.Model):
    rut = models.CharField(max_length=10)
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    telefono = models.CharField(max_length=20)
    email = models.CharField(max_length=40)

    def __str__(self):
        return ('{} {}'.format(self.nombre, self.apellidos))

class Medico(Persona):
    especialidad = models.CharField(max_length=80)
    foto_perfil = models.ImageField(upload_to='medicos', default='medicos/default.jpg') #foto idealmente de 400 x 415
    OPCIONES_GENERO = [
    ('F', 'Femenino'),
    ('M','Masculino'),
    ]
    genero = models.CharField(max_length=20, choices=OPCIONES_GENERO, default='M')

    def __str__(self):
        if self.genero == 'M':
            return('Dr. {} {} - {}'.format(self.nombre, self.apellidos, self.especialidad))
        else:
            return('Dra. {} {} - {}'.format(self.nombre, self.apellidos, self.especialidad))

class Paciente(Persona):
    fecha_nacimiento = models.DateField(blank=True, null=True)

    def __str__(self):
        return('{} {}'.format(self.nombre, self.apellidos))

class Cita_medica(models.Model):
    fecha_cita = models.DateField(blank=True, null=True)
    hora_inicio_cita = models.TimeField()
    hora_fin_cita = models.TimeField()
    OPCIONES_ESTADO_CITA = [
    ('DIS', 'Disponible'),
    ('SEL', 'Seleccionada'),
    ('RES', 'Reservada'),
    ('CONF','Confirmada'),
    ('ANUL', 'Anulada'),
    ('REA', 'Realizada'),
    ]
    estado_cita = models.CharField(max_length=20, choices=OPCIONES_ESTADO_CITA, default='DIS')
    medico = models.ForeignKey('Medico', on_delete=models.CASCADE)
    paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE, blank=True, null=True)
    fecha_actualizacion = models.DateField(blank=True, null=True)

    def __str__(self):
        return('Médico: {} | Paciente: {} | Fecha: {} | Hora: {}'.format(self.medico, self.paciente, self.fecha_cita, self.hora_inicio_cita))
