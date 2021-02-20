from rest_framework import serializers
from .models import courses,User,require

class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = courses
        fields = ('id','coursename', 'courseid')
#visit the endpoint via GET 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','phone_number','email','course')
class requireSerializer(serializers.ModelSerializer):
    class Meta:
        model = require
        fields = ('id','coursereq','coursegiv','user')
        