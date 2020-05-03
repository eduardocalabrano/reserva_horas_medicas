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

    def __str__(self):
        return('Dr.{} {} - {}'.format(self.nombre, self.apellidos, self.especialidad))

class Paciente(Persona):
    fecha_nacimiento = models.DateField(blank=True, null=True)

    def __str__(self):
        return('{} {}'.format(self.nombre, self.apellidos))

class Cita_medica(models.Model):
    fecha_cita = models.DateField(blank=True, null=True)
    hora_inicio_cita = models.TimeField()
    hora_fin_cita = models.TimeField()
    OPCIONES_ESTADO_CITA = [
    ('SOL', 'Solicitada'),
    ('CONF','Confirmada'),
    ('ANUL', 'Anulada'),
    ('REA', 'Realizada'),
    ]
    estado_cita = models.CharField(max_length=20, choices=OPCIONES_ESTADO_CITA, default='SOL')
    medico = models.ForeignKey('Medico', on_delete=models.CASCADE)
    paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE)

    def __str__(self):
        return('Médico: {} | Paciente: {} | Fecha: {} | Hora: {}'.format(self.medico, self.paciente, self.fecha_cita, self.hora_inicio_cita))