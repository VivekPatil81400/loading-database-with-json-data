from django.db import models
from django.core.validators import MaxLengthValidator

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=20)
    sector = models.CharField(max_length=10)
    siren = models.IntegerField()
    ca = models.IntegerField()
    margin = models.IntegerField()
    ebitda = models.IntegerField()
    loss = models.IntegerField()
    year = models.IntegerField()

    def __str__(self):
        return self.name