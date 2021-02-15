# views.py
from rest_framework import viewsets

from .serializers import CoursesSerializer,UserSerializer
from .models import courses,User


class CoursesViewSet(viewsets.ModelViewSet):
    queryset = courses.objects.all().order_by('coursename')
    serializer_class = CoursesSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer