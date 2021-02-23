from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class courses(models.Model):
	
	coursename=models.CharField(max_length=64)
	courseid=models.CharField(max_length=64, primary_key = True)
	def __str__(self):
		return self.coursename

class User(AbstractUser):
	phone_number = models.CharField(max_length=12)
	userid = models.CharField(max_length=255 ,primary_key = True)
	course = models.ManyToManyField(courses,blank=True)
	pass
	def __str__(self):
		return self.userid
class require(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="user")
	coursereq=models.ForeignKey(courses,on_delete=models.CASCADE,related_name="coursereq")
	coursegiv=models.ForeignKey(courses,on_delete=models.CASCADE,related_name="coursegiv")
	
