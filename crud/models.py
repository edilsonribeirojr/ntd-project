from django.db import models

class Planets(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=30,
        blank=False,
        null=False,
        default='Unnamed Planet',)
    population = models.IntegerField(
        blank=True,
        null=True,
    )
    terrains = models.CharField(
        max_length=100,
        blank=True,
        null=True,)
    climates = models.CharField(
        max_length=100,
        blank=True,
        null=True)

    def __str__(self):
        return self.name