#from django.db import models
from django.contrib.gis.db import models

# Create your models here.

class Shop(models.Model):
    """Models for Shop table"""
    print("__entered shops/models.py__")
    name = models.CharField(max_length=100)

    ##Geodjango feature for point geometry
    location = models.PointField()

    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
