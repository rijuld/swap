from rest_framework import serializers
from .models import courses

class CoursesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = courses
        fields = ('id','coursename', 'courseid')
#visit the endpoint via GET 
