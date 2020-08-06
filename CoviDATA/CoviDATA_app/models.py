from django.db import models

class illustrate(models.Model):
    name = models.CharField(max_length=32)
    image = models.ImageField(blank = True, null = True)

class estate(models.Model):
    name = models.CharField(max_length=32)
    image = models.ImageField(blank = True, null = True)
    casos = models.IntegerField()
    recuperados = models.IntegerField()
    obitos = models.IntegerField()
    medmov_casos = models.IntegerField()
    medmov_obitos = models.IntegerField()
    


# Create your models here.
