from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('medicos/<esp>/', views.listar_medicos, name='listar_medicos'),
    path('ajax/fechas_disponibles/', views.fechas_disponibles, name='fechas_disponibles'),
    path('ajax/horas_disponibles/', views.horas_disponibles, name='horas_disponibles'),
    path('ajax/ingresa_paciente/', views.ingresa_paciente, name='ingresa_paciente'),

]
