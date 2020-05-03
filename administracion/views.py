from django.shortcuts import render

def inicio(request):
    return render(request, 'administracion/inicio.html', {})
