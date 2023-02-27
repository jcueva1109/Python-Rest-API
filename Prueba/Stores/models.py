from django.db import models

# Create your models here.
class Store(models.Model):
    id = models.IntegerField(primary_key=True)
    brand = models.IntegerField()
    identifier = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

class Brand(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    logo = models.URLField()