from django.shortcuts import render
from django.urls import reverse_lazy
# Create your views here.

# ------------------------------------------------------------------
# APIS
# ------------------------------------------------------------------
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    # DetailView
    RetrieveAPIView,
    # Delete
    DestroyAPIView,
    # Actualizar
    UpdateAPIView,
    # Recupera y actualiza
    RetrieveUpdateAPIView,
    # Recupera y elimina
    RetrieveDestroyAPIView,
)

from .serializer import (
    TrabajosSerializer,
    DepartamentosSerializer,
)
# ------------------------------------------------------------------
# VISTAS A USAR
# ------------------------------------------------------------------

from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# ------------------------------------------------------------------
# MODELOS
# ------------------------------------------------------------------
from .models import Departamento, Trabajo

# ------------------------------------------------------------------
# FORMULARIOS
# ------------------------------------------------------------------

from .forms import NuevoDepartamentoForm

# ------------------------------------------------------------------
# CREAR DEPARTAMENTO
# ------------------------------------------------------------------

class NuevoDepartamento(CreateView):
    # Modelo usado para la vista
    model = Departamento
    # Template usado en la vista
    template_name = 'departamento/NuevoDepartamento.html'
    # Contexto usado para la impresión en el html
    context_object_name = 'NuevoDepartamento'
    # formulario usado en la vista
    form_class = NuevoDepartamentoForm
    # Dirección a la que va cuando se ejecuta el submit
    success_url = reverse_lazy('inicio_app:home')

    def form_valid(self, form):
        # Guardando los datos del formulario
        departament = form.save(commit=False)
        departament.save()
        # Return del formulario completado
        return super(NuevoDepartamento, self).form_valid(form)

# ------------------------------------------------------------------
# API CREAR UN TRABAJO
# ------------------------------------------------------------------
class TrabajoAPISerializer(CreateAPIView):
    serializer_class = TrabajosSerializer

# ------------------------------------------------------------------
# API CREAR UN TRABAJO
# ------------------------------------------------------------------
class DepartamentoAPISerializer(CreateAPIView):
    serializer_class = DepartamentosSerializer