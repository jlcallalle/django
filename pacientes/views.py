from django.shortcuts import render
from django.views.generic import ListView
from .models import Pacientes

class ListarPacientes(ListView):
    template_name = 'listar-paciente.html'
    model = Pacientes
    context_object_name = 'pacientes'

# Create your views here.
#def ListarPacientes(request):
#    pacientes = Pacientes.objects.all()
#    return render(request, "listar-paciente.html", {'pacientes': pacientes})


