# ------------------------------------------------------------------
# DJANGO
# ------------------------------------------------------------------

from django import forms

# ------------------------------------------------------------------
# MODELO
# ------------------------------------------------------------------

from .models import LanguageInfo

# ------------------------------------------------------------------
# FORMULARIO
# ------------------------------------------------------------------
class NewLanguageInfoForm(forms.ModelForm):
    """Form definition for LanguageInfo."""
    class Meta:
        """Meta definition for LanguageInfoform."""
        # Modelo al que se aplica el formulario
        model = LanguageInfo
        # Campos usados en el formulario
        fields = (
            'language',
            'isOfficial',
            'Percentege',
            'ISOCode',
            'languageLevel',
        )
        # Labels de los campos del formulario
        labels = {
            'Language': 'Nombre Lenguaje',
            'isOfficial': 'activate',
            'Percentege': 'Porcentaje',
            'ISOCode': 'Codigo ISO',
            'languageLevel': 'Nivel de lenguaje',
        }
                # Espacio para agregar características a los campos
        widgets = {
            'Language': forms.TextInput(
                attrs={'class': 'ContainerLanguageInfoFormSelect',
                        'placeholder':'Nombre de ciudad'}
            ),
            'isOfficial': forms.CheckboxInput(
                attrs={
                    'class': 'ContainerLanguageInfoFormName',
                }
            ),
            'Percentege': forms.TextInput(
                attrs={
                    'class': 'ContainerLanguageInfoFormName',
                    'placeholder': 'Porcentaje'
                }
            ),
            'ISOCode': forms.TextInput(
                attrs={
                    'class': 'ContainerLanguageInfoFormName',
                    'placeholder': 'Codigo ISO '
                }
            ),
            'languageLevel': forms.TextInput(
                attrs={
                    'class': 'ContainerLanguageInfoFormName',
                    'placeholder': 'Nivel de lenguaje'
                }
            ),
        }