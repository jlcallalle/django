# Generated by Django 2.2.4 on 2019-08-28 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pacientes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_documento', models.CharField(choices=[('DNI', 'DNI'), ('CE', 'Carné de Extranjería'), ('IN', 'Indocumentado')], default='DNI', max_length=3)),
                ('numero_documento', models.CharField(max_length=100, unique=True)),
                ('nombres', models.TextField()),
                ('appPaterno', models.CharField(max_length=100)),
                ('appMaterno', models.CharField(max_length=100)),
                ('fecha', models.DateField()),
            ],
        ),
    ]
