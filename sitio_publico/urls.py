from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('medicos/<esp>/', views.listar_medicos, name='listar_medicos'),
    # path('post/<int:pk>/', views.post_detail, name='post_detail'),
]