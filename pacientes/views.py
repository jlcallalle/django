from django.shortcuts import render
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy, reverse
from .models import Pacientes
from .form import PacienteForm, BuscarPacienteForm


class ListarPacientes(FormView, ListView):
    template_name = 'listar-paciente.html'
    model = Pacientes
    context_object_name = 'pacientes'
    form_class = BuscarPacienteForm
    form = BuscarPacienteForm
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        pacientes = []
        form.is_valid()
        encontro =0
        tipo_documento = form.cleaned_data.get('tipo_documento')
        numero_documento = form.cleaned_data.get('numero_documento')
        try:
            pacientes = [Pacientes.objects.get(
                tipo_documento=request.POST.get('tipo_documento'),
                numero_documento=request.POST.get('numero_documento')
            )]
            encontro=1
        except:
            pacientes=''
        return render(request, 'listar-paciente.html', {'form': form, 'pacientes': pacientes, 'encontro': encontro})

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

