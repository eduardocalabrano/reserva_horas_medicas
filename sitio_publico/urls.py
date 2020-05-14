from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('medicos/<esp>/', views.listar_medicos, name='listar_medicos'),
    path('ajax/retorna_horasdisponibles/', views.horas_disponibles, name='horas_disponibles'),
]
