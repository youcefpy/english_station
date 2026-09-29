from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class MyUser(AbstractUser):
    pass

class Admin(MyUser):
    pass
class Student(MyUser):
    pass

class AcadimicLevel(models.IntegerChoices):
    FIRST_YEAR = 1
    SECOND_YEAR = 2
    THIRD_LEVEL = 3

class Stream(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    level = models.IntegerField(choices=AcadimicLevel.choices)

    def __str__(self):
        return f"Stream: {self.name}, {self.description}, {self.level}"
class Unit(models.Model):
    name=  models.CharField(max_length=255)
    description = models.TextField()

class Cours(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    unit = models.ForeignKey(Unit,on_delete=models.CASCADE)
    stream = models.ForeignKey(stream, on_delete=models.CASCADE)
    format = models.CharField(max_length=255,default='.pdf')

class Exam(models.Model):
    ...

class Question(models.Model):
    ...