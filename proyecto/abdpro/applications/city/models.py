from django.db import models
from applications.country.models import Country


class City(models.Model):
    name = models.CharField(
        'Name',
        null=False,
        max_length=30,
        default=''
    )

    countryCode = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
    )

    district = models.CharField(
        'District',
        max_length=20,
        null=False,
        default=''
    )

    population = models.IntegerField(
        'Population',
        null=False,
        default=0
    )

    securityRate = models.DecimalField(
        'SecurityRate',
        max_digits=5,
        decimal_places=2,
        null=False,
        default=0.00
    )

    pollutionRate = models.DecimalField(
        'PollutionRate',
        max_digits=5,
        decimal_places=2,
        null=False,
        default=0.00
    )

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'
        ordering = ['name']
        unique_together = ('name', 'countryCode')

    def __str__(self):
        return f"{self.name} - {self.countryCode} - {self.id}"


