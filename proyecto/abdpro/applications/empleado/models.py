from django.db import models
from applications.departamento.models import Departamento, Trabajo

# Create your models here.
class Habilidad(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)
    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades'

class Empleado(models.Model):
    nombres = models.CharField('Nombres', max_length=50)
    apellidos = models.CharField('Apellidos', max_length=50)
    trabajo = models.ForeignKey(Trabajo, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    hv = models.CharField('hv', max_length=50)
    avatar = models.ImageField(
        upload_to='empleados', blank=True, null=True)
    habilidades = models.ManyToManyField(Habilidad)
    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
    def __str__(self):
        return self.apellidos+' ' + self.nombres + ' - ' + str(self.id)