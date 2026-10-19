from csv import list_dialects

from django.contrib import admin

from .models import Admin, Student

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display  = ('first_name','last_name','email', 'level', 'stream')


class ControlAdmin(admin.ModelAdmin):
    ...

admin.site.register(Student,StudentAdmin)
admin.site.register(Admin,ControlAdmin)
