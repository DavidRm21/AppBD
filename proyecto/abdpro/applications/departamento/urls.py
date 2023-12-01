from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "departamento_app"

urlpatterns = [
        path('NuevoDepartamento/',
                views.NuevoDepartamento.as_view(),
                name='NuevoDepartamento'),
        path('TrabajoAPISerializer/',
                views.TrabajoAPISerializer.as_view(),
                name='TrabajoAPISerializer'),
        path('DepartamentoAPISerializer/',
                views.DepartamentoAPISerializer.as_view(),
                name='DepartamentoAPISerializer'),
]
