from django.contrib.auth.models import AbstractUser
from django.db import models

from utils import AcadimicLevelChoices, StreamNameChoices

# Create your models here.

class User(AbstractUser):
    pass

class Student(User):
    level = models.IntegerField(choices=AcadimicLevelChoices)
    stream = models.CharField(choices=StreamNameChoices)
class Admin(User):


    def generate_token(self):
        """
        As Admin i check the new register of student.
        i check the information of the students.
        if student in the database of school:
            i send email to the student where in the email i have a url
            redirect to set_password.html page
        else :
            igone the email
        This function generate
        token to new user and send the generated token to the student it will
        send the email to the student with the url and redirect to
        password and confirm password
        """
        print("Generate token for and send " \
        "email with link and when link " \
        "clicked it will redicrect to set password page")
