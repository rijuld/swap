from rest_framework import serializers
from .models import courses,User

class CoursesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = courses
        fields = ('id','coursename', 'courseid')
#visit the endpoint via GET 

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id','phone_number','email','course')