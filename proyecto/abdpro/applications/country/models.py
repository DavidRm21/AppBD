from django.db import models

class Country(models.Model):
    code = models.CharField(
        'code',
        null=False,
        max_length=7
    )
    
    name = models.CharField(
        'Name',
        null=False,
        max_length=50,
        unique=True
    )
    
    continent = models.CharField(
        'Continent',
        null=False,
        default='Asia'
    )
    
    region = models.CharField(
        'Region',
        null=False,
        max_length=26,
        default=''
    )
    
    surface_area = models.DecimalField(
        'SurfaceArea',
        null=False,
        max_digits=10,
        decimal_places=2,
        default=0.0
    )
    
    independence = models.SmallIntegerField(
        'IndepYear',
        null=False,
    )
    
    population = models.BigIntegerField(
        'Population',
        null=False,
        default=0
    )
    
    life_expectancy = models.DecimalField(
        'LifeExpectancy',
        null=False,
        max_digits=3,
        decimal_places=1,
        default=0.0
    )
    
    gnp = models.DecimalField(
        'GNP',
        null=True,
        max_digits=10,
        decimal_places=2,
        default=0.00
    )
    
    gnp_old = models.DecimalField(
        'GNPOld',
        null=True,
        max_digits=10,
        decimal_places=2,
        default=0.00
    )
    
    local_name = models.CharField(
        'LocalName',
        null=False,
        default='',
        max_length=50
    )
    
    government_form = models.CharField(
        'GovernmentForm',
        max_length=50,
        default=''
    )
    
    head_of_state = models.CharField(
        'HeadOfState',
        max_length=60,
        default=''
    )
    
    capital = models.IntegerField(
        'Capital',
        default=0
    )
    
    arable_land_area = models.DecimalField(
        'ArableLandArea',
        null=False,
        max_digits=10,
        decimal_places=2,
        default=0.00
    )
    
    hdi = models.DecimalField(
        'HDI',
        max_digits=5,
        decimal_places=3,
        default=0.0
    )
    
    national_currency = models.CharField(
        'NationalCurrency',
        null=False,
        max_length=4,
        default=''
    )
    
    search_fields = ('name', 'code',)
    list_filter = ('name',)
    
    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'
        ordering = ['name']
        unique_together = ('name', 'code')
    
    def __str__(self):
        return f"{self.name} - {self.code} - {self.id}"
