from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
GENDER = [
    ("M" , "Male"),
    ("F" , "Female"),
]

class CustomUser(AbstractUser):
    age = models.IntegerField()
    gender = models.CharField(max_length=1 , choices=GENDER)
    weight = models.FloatField()
    height = models.FloatField()
    weight_goal = models.FloatField()

    def __str__(self):
        return self.username
    
    