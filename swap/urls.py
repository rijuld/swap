# myapi/urls.py
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'courses', views.CoursesViewSet)
router.register(r'users', views.NewUserViewSet)
router.register(r'require', views.RequireViewSet)
router.register(r'authtok', views.authtokViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]