from django import forms
from .models import Pacientes


class BuscarPacienteForm(forms.Form):
    cbo_doc = (
          ('DNI', 'DNI'),
          ('CE', 'Carné de Extranjería'),
          ('IN', 'Indocumentado'),
    )
    tipo_documento = forms.ChoiceField(label='Tipo de documento',
                                       choices=cbo_doc, initial='1',
                                       required=False,
                                       widget=forms.Select(attrs={'class': 'form-control jorge', }))
    numero_documento = forms.CharField(label='Número de documento', max_length=15, min_length=8,
                                       widget=forms.TextInput(attrs={
                                           'placeholder': ''}), required=False)


class PacienteForm(forms.models.ModelForm):
    class Meta:
        model = Pacientes
        fields = '__all__'
        widgets = {
                'fechaDeNacimiento': forms.DateInput(attrs={'type': 'date'}),
                'fecha': forms.TextInput(attrs={
                    'class': 'form-control holafecha', 'maxlength': '20', 'type': 'date'}),
                    #'class': 'form-control holafecha', 'maxlength': '20', 'autocomplete': 'off'}),
                }

        labels = {
                'tipo_documento': 'Tipo de Documento',
                'numero_documento': 'Número de Documento',
                'nombres': 'Nombres',
                'appPaterno': 'Apellido Paterno',
                'appMaterno': 'Apellido Materno',
                'fecha': 'Fecha Nacimiento',
                }

    def clean_numero_documento(self):
        data = self.cleaned_data['numero_documento']
        if len(data) < 8:
            raise forms.ValidationError("ingrese  caracteres")

        # Always return a value to use as the new cleaned data, even if
        # this method didn't change it.
        return data