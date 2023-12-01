# ------------------------------------------------------------------
# DJANGO
# ------------------------------------------------------------------

from django import forms

# ------------------------------------------------------------------
# MODELO
# ------------------------------------------------------------------

from .models import Country

# ------------------------------------------------------------------
# FORMULARIO
# ------------------------------------------------------------------
class NewCountryForm(forms.ModelForm):
    """Form definition for Country."""
    class Meta:
        """Meta definition for Countryform."""
        # Modelo al que se aplica el formulario
        model = Country
        # Campos usados en el formulario
        fields = (
            'code',
            'name',
            'continent',
            'region',
            'surface_area',
            'independence',
            'population',
            'life_expectancy',
            'gnp',
            'gnp_old',
            'local_name',
            'government_form',
            'head_of_state',
            'capital',
            'arable_land_area',
            'hdi',
            'national_currency',
        )
        # Labels de los campos del formulario
        labels = {
            'code': 'CodigoCountry',
            'name': 'NombreCountry',
            'continent': 'Continente',
            'region': 'Region',
            'surface_area': 'Superficie',
            'independence': 'DiaIndependencia',
            'population': 'Poblacion',
            'life_expectancy': 'EsperanzaVida',
            'gnp': 'ProductoBruto',
            'gnp_old': 'ProductoBrutoAnterior',
            'local_name': 'NombreLocal',
            'government_form': 'FormaGobierno',
            'head_of_state': 'JefeEstado',
            'capital': 'Capital',
            'arable_land_area': 'TierraCultivable',
            'hdi': 'HDI',
            'national_currency': 'MonedaNacional',
        }
                # Espacio para agregar características a los campos
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'ContainerCityFormSelect',
                        'placeholder':'Nombre de Pais'}
            ),
            'continent': forms.TextInput(
                attrs={
                    'class': 'ContainerCityFormName',
                    'placeholder': 'Distrito'
                }
            ),
            'region': forms.TextInput(
                attrs={
                    'class': 'ContainerCityFormName',
                    'placeholder': 'Poblacion'
                }
            ),
            'surface_area': forms.TextInput(
                attrs={
                    'class': 'ContainerCityFormName',
                    'placeholder': 'Indice de Seguridad '
                }
            ),
            'independence': forms.TextInput(
                attrs={
                    'class': 'ContainerCityFormName',
                    'placeholder': 'Indice de contaminacion'
                }
            ),
        }