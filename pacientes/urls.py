from django.urls import path, include
from .views import ListarPacientes, CrearPacientes, EditarPacientes, EliminarPacientes, TesteandoView

urlpatterns = [
    path('aaa/', ListarPacientes.as_view(), name="listar-pacientes"),
    path('', TesteandoView.as_view(), name="prueba"),
    path('crear/', CrearPacientes.as_view(), name="crear-pacientes"),
    path('editar/<int:pk>', EditarPacientes.as_view(), name="editar-pacientes"),
    path('eliminar-pacientes/<int:pk>', EliminarPacientes.as_view(), name="eliminar-pacientes"),

]