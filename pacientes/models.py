from django.db import models
from datetime import datetime
from dateutil.relativedelta import relativedelta

class Pacientes(models.Model):
    tipo_documento = models.CharField(max_length=3, choices=[
        ('DNI', 'DNI'),
        ('CE', 'Carné de Extranjería'),
        ('IN', 'Indocumentado'),
    ], default='DNI')
    numero_documento = models.CharField(max_length=100)
    nombres = models.TextField()
    appPaterno = models.CharField(max_length=100)
    appMaterno = models.CharField(max_length=100)
    fecha = models.DateField()

    class Meta:
        unique_together = ('tipo_documento', 'numero_documento')

    @property
    def edad(self):
        if not self.fecha:
            return ''
        edad1 = relativedelta(datetime.now().date(), self.fecha)
        if edad1.years < 1:
            if edad1.months <= 1:
                res = '{month} meses {day} días'.format(month=edad1.months, day=edad1.days)
            else:
                res = '{month} meses {day} días'.format(month=edad1.months, day=edad1.days)
        else:
            res = '{year} años, {month} meses {day} días'.format(year=edad1.years, month=edad1.months, day=edad1.days)

        return res

