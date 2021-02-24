from rest_framework import serializers
from .models import courses,NewUser,require

class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = courses
        fields = ('coursename', 'courseid')
#visit the endpoint via GET 

class NewUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = ('phone_number','userid')
class requireSerializer(serializers.ModelSerializer):
    class Meta:
        model = require
        fields = ('id','coursereq','coursegiv','user')

        