from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class courses(models.Model):
	
	coursename=models.CharField(max_length=64)
	courseid=models.CharField(max_length=64)

	def __str__(self):
		return self.coursename
class User(AbstractUser):
	phone_number = models.CharField(max_length=12)
	usersname = models.CharField(max_length=64)
	course = models.ManyToManyField(courses)
	pass
	def __str__(self):
		return self.username
class require(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="user")
	coursereq=models.ForeignKey(courses,on_delete=models.CASCADE,related_name="coursereq")
	coursegiv=models.ForeignKey(courses,on_delete=models.CASCADE,related_name="coursegiv")
		