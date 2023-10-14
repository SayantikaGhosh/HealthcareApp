from django.db import models

class Food(models.Model):
    foodname = models.CharField(max_length=100)
    calories = models.IntegerField(null=True)
    fat = models.FloatField(default=0.0,null=True)
    carbs = models.FloatField(default=0.0,null=True)
    protein = models.FloatField(default=0.0,null=True)
    fibres = models.FloatField(default=0.0,null=True)
