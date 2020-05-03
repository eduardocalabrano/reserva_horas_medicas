from django.contrib import admin
from .models import Medico, Paciente, Cita_medica

# admin.site.register(Persona)
admin.site.register(Medico)
admin.site.register(Paciente)
admin.site.register(Cita_medica)

