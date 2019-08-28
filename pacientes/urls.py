from django.urls import path, include
from . import views
from .views import ListarPacientes

urlpatterns = [
    path('', ListarPacientes.as_view()),
]