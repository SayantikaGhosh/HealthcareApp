from django.db import models
from django.contrib.auth.models import User

class Food(models.Model):
    foodname = models.CharField(max_length=100)
    calories = models.IntegerField(null=True)
    fat = models.FloatField(default=0.0,null=True)
    carbs = models.FloatField(default=0.0,null=True)
    protein = models.FloatField(default=0.0,null=True)
    fibres = models.FloatField(default=0.0,null=True)

class Consume(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    foodconsumed = models.ForeignKey(Food, on_delete=models.CASCADE)