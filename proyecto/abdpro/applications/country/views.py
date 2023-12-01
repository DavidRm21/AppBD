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
    CountrySerializer
)
# ------------------------------------------------------------------
# VISTAS A USAR
# ------------------------------------------------------------------

from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# ------------------------------------------------------------------
# MODELOS
# ------------------------------------------------------------------
from .models import Country

# ------------------------------------------------------------------
# FORMULARIOS
# ------------------------------------------------------------------

from .forms import NewCountryForm

# ------------------------------------------------------------------
# CREAR Country
# ------------------------------------------------------------------

class NewCountry(CreateView):
    # Modelo usado para la vista
    model = Country
    # Template usado en la vista
    template_name = 'Country/NewCountry.html'
    # Contexto usado para la impresión en el html
    context_object_name = 'NewCountry'
    # formulario usado en la vista
    form_class = NewCountryForm
    # Dirección a la que va cuando se ejecuta el submit
    success_url = reverse_lazy('inicio_app:home')

    def form_valid(self, form):
        # Guardando los datos del formulario
        country = form.save(commit=False)
        country.save()
        # Return del formulario completado
        return super(NewCountry, self).form_valid(form)

# ------------------------------------------------------------------
# API CREAR UN TRABAJO
# ------------------------------------------------------------------
class CountryAPISerializer(CreateAPIView):
    serializer_class = CountrySerializer