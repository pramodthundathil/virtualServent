from django.db import models

class MenuCard(models.Model):
    name = models.CharField(max_length=255)
    NonVegdiet = models.BooleanField(default=False)
    description = models.CharField(max_length=255)
    Price = models.FloatField()
    is_avilable = models.BooleanField(default=True)
    quantity = models.CharField(max_length=255)
