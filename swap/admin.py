from django.contrib import admin
from .models import User,courses,require
# Register your models here.
admin.site.register(User)
admin.site.register(courses)
admin.site.register(require)