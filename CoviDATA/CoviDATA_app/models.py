from django.db import models

class illustrate(models.Model):
    name = models.CharField(max_length=32)
    image = models.ImageField(blank = True, null = True)

class estate(models.Model):
    name = models.CharField(max_length=32)
    image = models.ImageField(blank = True, null = True)
    


# Create your models here.
