from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView

class InicioTemplateView(TemplateView):
    # Template usado en la vista
    template_name = "inicio/InicioTemplateView.html"
    # Contexto usado para la impresión en el html
    context_object_name = 'InicioTemplateView'