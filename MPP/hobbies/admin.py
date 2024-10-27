from django.contrib import admin
from .models import Programme, Mentor, Student

# Register your models here.
admin.site.register(Mentor)
admin.site.register(Student)