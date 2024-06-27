from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Prediction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    area = models.FloatField()
    bedrooms = models.IntegerField()
    predicted_price = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)