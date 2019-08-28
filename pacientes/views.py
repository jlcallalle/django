from django.shortcuts import render
from django.views.generic import ListView, DeleteView
from django.urls import reverse_lazy, reverse
from .models import Pacientes

class ListarPacientes(ListView):
    template_name = 'listar-paciente.html'
    model = Pacientes
    context_object_name = 'pacientes'

class EliminarPacientes(DeleteView):
    template_name = 'eliminar-paciente.html'
    model = Pacientes
    success_url = reverse_lazy('listar-pacientes')

# Create your views here.
#def ListarPacientes(request):
#    pacientes = Pacientes.objects.all()
#    return render(request, "listar-paciente.html", {'pacientes': pacientes})


