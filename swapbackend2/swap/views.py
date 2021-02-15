# views.py
from rest_framework import viewsets

from .serializers import CoursesSerializer
from .models import courses


class CoursesViewSet(viewsets.ModelViewSet):
    queryset = courses.objects.all().order_by('coursename')
    serializer_class = CoursesSerializer