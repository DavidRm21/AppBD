from rest_framework import serializers, pagination

from .models import(
    Departamento,
    Trabajo
)

class TrabajosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trabajo
        fields = ('__all__')

class DepartamentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = ('__all__')