from django.db import models

class illustrate(models.Model):
    name = models.CharField(max_length=32)
    image = models.ImageField(blank = True, null = True)

class estate(models.Model):
    name = models.CharField(max_length=32)
   
    casos = models.IntegerField(blank = True, null = True)
    obitos = models.IntegerField(blank = True, null = True)
    recuperados = models.IntegerField(blank = True, null = True)
    media_movel_casos = models.FloatField(blank = True, null = True)
    media_movel_obitos = models.FloatField(blank = True, null = True)



# Create your models here.
