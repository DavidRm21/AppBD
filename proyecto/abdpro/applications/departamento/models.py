from django.db import models

# Create your models here.
class Departamento(models.Model):
    nombreDepartamento = models.CharField('nombreDepartamento', max_length=50)
    siglaDepartamento = models.CharField(
        'siglaDepartamento', max_length=2, unique=True)
    activoDepartamento = models.BooleanField('active', default=False)
    search_fields = ('nombreDepartamento', 'siglaDepartamento',)
    list_filter = ('nombreDepartamento',)
    class Meta:
            verbose_name = 'Nombre Departamento'
            verbose_name_plural = 'Nombres Departamentos'
            ordering = ['nombreDepartamento']
            unique_together = ('nombreDepartamento', 'siglaDepartamento')
    def __str__(self):
        return self.nombreDepartamento + ' - ' + self.siglaDepartamento + str(self.id)

class Trabajo(models.Model):
    nombreTrabajo = models.CharField('nombreTrabajo', max_length=50)
    siglaTrabajo = models.CharField(
        'siglaTrabajo', max_length=2, unique=True)
    activoTrabajo = models.BooleanField('active', default=False)
    search_fields = ('nombreTrabajo', 'siglaTrabajo',)
    list_filter = ('nombreTrabajo',)
    class Meta:
        verbose_name = 'Trabajo'
        verbose_name_plural = 'Trabajos'
        ordering = ['nombreTrabajo']
        unique_together = ('nombreTrabajo', 'siglaTrabajo')
        def __str__(self):
            return self.nombreTrabajo + ' - ' + self.siglaTrabajo + str(self.id)
