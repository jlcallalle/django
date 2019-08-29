from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('', include('pacientes.urls')),
    path('admin/', admin.site.urls),
    re_path(r'^', include('minsalogin.urls', namespace='auth')),
]
