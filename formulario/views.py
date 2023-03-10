from django.shortcuts import render, redirect
from .models import Estudiante
from .forms import EstudianteForm

def index(request):
    return render(request, 'index.html')

def crear_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('estudiante_creado')
    else:
        form = EstudianteForm()
    return render(request, 'crear_estudiante.html', {'form': form})

def estudiante_creado(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'lista_estudiantes.html', {'estudiantes': estudiantes})

def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'lista_estudiantes.html', {'estudiantes': estudiantes})

