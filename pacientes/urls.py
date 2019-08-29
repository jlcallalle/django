from django.urls import path, include
from .views import ListarPacientes, CrearPacientes, EditarPacientes, EliminarPacientes

urlpatterns = [
    path('', ListarPacientes.as_view(), name="listar-pacientes"),
    path('crear/', CrearPacientes.as_view(), name="crear-pacientes"),
    path('editar/<int:pk>', EditarPacientes.as_view(), name="editar-pacientes"),
    path('eliminar/<int:pk>', EliminarPacientes.as_view(), name="eliminar-pacientes"),
]