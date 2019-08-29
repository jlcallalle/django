from django.shortcuts import render
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .models import Pacientes
from .form import PacienteForm

class ListarPacientes(ListView):
    template_name = 'listar-paciente.html'
    model = Pacientes
    context_object_name = 'pacientes'

class CrearPacientes(CreateView):
    template_name = 'crear-paciente.html'
    model = Pacientes
    form_class = PacienteForm
    form = PacienteForm
    #success_url = reverse_lazy('listar-pacientes')

    def get_success_url(self):
        messages.success(self.request, 'Se guardó exitosamente')
        return reverse('listar-pacientes')

class EliminarPacientes(DeleteView):
    template_name = 'eliminar-paciente.html'
    model = Pacientes
    success_url = reverse_lazy('listar-pacientes')

class EditarPacientes(UpdateView):
    template_name = 'editar-paciente.html'
    model = Pacientes
    form_class = PacienteForm
    success_url = reverse_lazy('listar-pacientes')

