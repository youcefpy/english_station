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
    ...
class Unit(models.Model):
    ...

class Cours(models.Model):
    ...
class Exam(models.Model):
    ...

class Question(models.Model):
    ...