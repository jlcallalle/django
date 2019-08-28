from django.urls import path, include
from .views import ListarPacientes, EliminarPacientes

urlpatterns = [
    path('', ListarPacientes.as_view(), name="listar-pacientes"),
    path('eliminar/<int:pk>', EliminarPacientes.as_view(),name="eliminar-pacientes"),
]