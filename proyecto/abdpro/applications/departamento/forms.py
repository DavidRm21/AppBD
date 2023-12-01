# ------------------------------------------------------------------
# DJANGO
# ------------------------------------------------------------------

from django import forms

# ------------------------------------------------------------------
# MODELO
# ------------------------------------------------------------------

from .models import Departamento

# ------------------------------------------------------------------
# FORMULARIO
# ------------------------------------------------------------------
class NuevoDepartamentoForm(forms.ModelForm):
    """Form definition for Empleado."""
    class Meta:
        """Meta definition for Empleadoform."""
        # Modelo al que se aplica el formulario
        model = Departamento
        # Campos usados en el formulario
        fields = (
            'nombreDepartamento',
            'siglaDepartamento',
            'activoDepartamento',
        )
        # Labels de los campos del formulario
        labels = {
            'nombreDepartamento': 'Nombre Departamento',
            'siglaDepartamento': 'Sigla Departamento',
            'activoDepartamento': 'Activo',
        }
                # Espacio para agregar características a los campos
        widgets = {
            'activoDepartamento': forms.CheckboxInput(
                attrs={'class': 'ContainerEmpleadoFormSelect'}
            ),
            'nombreDepartamento': forms.TextInput(
                attrs={
                    'class': 'ContainerEmpleadoFormName',
                    'placeholder': 'Nombre Departamento'
                }
            ),
            'siglaDepartamento': forms.TextInput(
                attrs={
                    'class': 'ContainerEmpleadoFormName',
                    'placeholder': 'Sigla Departamento'
                }
            ),
        }