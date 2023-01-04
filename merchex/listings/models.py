from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Band(models.Model):

    def __str__(self):
        return f'{self.name}'

    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'
        CLASSIC = 'CLA'
        ROCK = 'RO'
        PROGRESSIVE_ROCK = 'PR'

    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices=Genre.choices, max_length=50)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(
        validators=[MinValueValidator(1700), MaxValueValidator(2021)]
    )
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)


class Listing(models.Model):

    def __str__(self):
        return f'{self.title}'

    class Type(models.TextChoices):
        RECORDS = 'R'
        CLOTHING = 'C'
        POSTERS = 'P'
        MISC = 'M'

    title = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=1000)
    sold = models.fields.BooleanField(default=True)
    year_formed = models.fields.IntegerField()
    type = models.fields.CharField(choices=Type.choices, max_length=50)
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)


class About(models.Model):

    def __str__(self):
        return f'{self.title}'

