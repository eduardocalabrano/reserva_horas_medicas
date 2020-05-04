from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('medicos', views.listar_medicos, name='listar_medicos'),
]