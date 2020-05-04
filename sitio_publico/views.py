from django.shortcuts import render

def inicio(request):
    return render(request, 'administracion/inicio.html', {})

def listar_medicos(request):
    return render(request, 'administracion/medicos_especialidad.html', {})

