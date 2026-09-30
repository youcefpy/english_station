from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
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
        return f"{self.name}"
class Unit(models.Model):
    name=  models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):

        return f"{self.name}"

class Cours(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    unit = models.ForeignKey(Unit,on_delete=models.CASCADE)
    stream = models.ForeignKey(Stream, on_delete=models.CASCADE)
    lesson = models.FileField(upload_to='lesson/', default="")
    
    def __str__(self):
        return f"{self.stream.name}: {self.unit.name} : {self.title}"

class Exam(models.Model):
    title = models.CharField(max_length=255)
    cours = models.ForeignKey(Cours,on_delete=models.CASCADE)
    passing_scrore = models.IntegerField(
        default=0,
        validators=[MinValueValidator(1), MaxValueValidator(10)]
        )

class Question(models.Model):
    ...