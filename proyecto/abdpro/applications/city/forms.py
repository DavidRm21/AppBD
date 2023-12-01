# ------------------------------------------------------------------
# DJANGO
# ------------------------------------------------------------------

from django import forms

# ------------------------------------------------------------------
# MODELO
# ------------------------------------------------------------------

from .models import City

# ------------------------------------------------------------------
# FORMULARIO
# ------------------------------------------------------------------
class NewCityForm(forms.ModelForm):
    """Form definition for City."""
    class Meta:
        """Meta definition for Cityform."""
        # Modelo al que se aplica el formulario
        model = City
        # Campos usados en el formulario
        fields = (
            'name',
            'district',
            'population',
            'securityRate',
            'pollutionRate',
        )
        # Labels de los campos del formulario
        labels = {
            'name': 'Nombre City',
            'district': 'Distrito',
            'population': 'Poblacion',
            'securityRate': 'Seguridad',
            'pollutionRate': 'Contaminacion',
        }
                # Espacio para agregar características a los campos
        widgets = {
            'Name': forms.TextInput(
                attrs={'class': 'ContainerCityFormSelect',
                        'placeholder':'Nombre de ciudad'}
            ),
            'nombreCity': forms.TextInput(
                attrs={
                    'class': 'ContainerCityFormName',
                    'placeholder': 'Distrito'
                }
            ),
            'Population': forms.TextInput(
                attrs={
                    'class': 'ContainerCityFormName',
                    'placeholder': 'Poblacion'
                }
            ),
            'SecurityRate': forms.TextInput(
                attrs={
                    'class': 'ContainerCityFormName',
                    'placeholder': 'Indice de Seguridad '
                }
            ),
            'PollutionRate': forms.TextInput(
                attrs={
                    'class': 'ContainerCityFormName',
                    'placeholder': 'Indice de contaminacion'
                }
            ),
        }