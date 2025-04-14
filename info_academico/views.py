from django.shortcuts import render
from .models import Materia

def index(request):
    materias_vista = Materia.objects.prefetch_related('libro_set', 'progreso_set')  # carga libros y progreso

    contexto = {
        'nombre_sitio': 'GramiSysLib',
        'materias': materias_vista
    }

    return render(request, 'info_academico/index.html', contexto)
