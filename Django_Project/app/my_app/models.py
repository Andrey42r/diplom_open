from django.db import models

# Create your models here.

class Trip(models.Model):
    distance = models.FloatField(default=0, null=True)
    fuel_consumption = models.FloatField(default=0, null=True)
    fuel_price = models.FloatField(default=0, null=True)

