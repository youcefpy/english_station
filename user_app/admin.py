from django.contrib import admin

from .models import Admin, Student

# Register your models here.


admin.site.register(Student)
admin.site.register(Admin)