from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
	pass

class courses(models.Model):

	coursename=models.CharField(max_length=64)
	courseid=models.CharField(max_length=64)
