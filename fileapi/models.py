from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    roll = models.IntegerField()
    mobile = models.IntegerField()
    email = models.EmailField(max_length=50)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=30)



class AdditionalInfo(models.Model)    :
    id = models.AutoField(primary_key=True)
    father_name=models.CharField(max_length=100)
    father_mobile=models.IntegerField()
    father_age=models.IntegerField()
    father_email=models.EmailField(max_length=100)