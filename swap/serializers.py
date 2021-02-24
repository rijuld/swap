from rest_framework import serializers
from .models import courses,User,require

class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = courses
        fields = ('coursename', 'courseid')
#visit the endpoint via GET 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('phone_number','userid')
class requireSerializer(serializers.ModelSerializer):
    class Meta:
        model = require
        fields = ('id','coursereq','coursegiv','user')

        