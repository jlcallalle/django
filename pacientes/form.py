from django import forms

from .models import Pacientes

class PacienteForm(forms.models.ModelForm):
    class Meta:
        model = Pacientes
        fields = '__all__'
        widgets = {
                'fechaDeNacimiento': forms.DateInput(attrs={'type':'date'})
                }
        labels = {
                'tipo_documento' : 'Tipo de Documento',
                'numero_documento' : 'Número de Documento',
                'nombres' : 'Nombres',
                'appPaterno' : 'Apellido Paterno',
                'appMaterno': 'Apellido Materno',
                'fecha' : 'Fecha Nacimiento',
                }