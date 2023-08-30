from django.db import models

from django.db.models import CASCADE


# Create your models here.
class City(models.Model):
    place=models.CharField(max_length=50)
    def __str__(self):
        return self.place


class Student(models.Model):
    Name=models.CharField(max_length=50)
    Age=models.IntegerField()
    Gender=models.CharField(max_length=50)
    Email=models.EmailField(max_length=50)
    MobileNumber=models.BigIntegerField()
    place = models.ForeignKey(City,on_delete=models.CASCADE)