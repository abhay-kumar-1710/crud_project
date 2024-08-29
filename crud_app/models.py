from django.db import models

# Create your models here.

class PersonData(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    qualification = models.CharField(max_length=10)
    gender = models.CharField(max_length=6)