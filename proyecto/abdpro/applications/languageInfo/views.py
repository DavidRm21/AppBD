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
    LanguageInfoSerializer
)
# ------------------------------------------------------------------
# VISTAS A USAR
# ------------------------------------------------------------------

from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# ------------------------------------------------------------------
# MODELOS
# ------------------------------------------------------------------
from .models import LanguageInfo

# ------------------------------------------------------------------
# FORMULARIOS
# ------------------------------------------------------------------

from .forms import NewLanguageInfoForm

# ------------------------------------------------------------------
# CREAR LanguageInfo
# ------------------------------------------------------------------

class NewLanguageInfo(CreateView):
    # Modelo usado para la vista
    model = LanguageInfo
    # Template usado en la vista
    template_name = 'LanguageInfo/NewLanguageInfo.html'
    # Contexto usado para la impresión en el html
    context_object_name = 'NewLanguageInfo'
    # formulario usado en la vista
    form_class = NewLanguageInfoForm
    # Dirección a la que va cuando se ejecuta el submit
    success_url = reverse_lazy('inicio_app:home')

    def form_valid(self, form):
        # Guardando los datos del formulario
        languageInfo = form.save(commit=False)
        languageInfo.save()
        # Return del formulario completado
        return super(NewLanguageInfo, self).form_valid(form)

# ------------------------------------------------------------------
# API CREAR UN TRABAJO
# ------------------------------------------------------------------
class LanguageInfoAPISerializer(CreateAPIView):
    serializer_class = LanguageInfoSerializer