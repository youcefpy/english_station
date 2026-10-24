from django.contrib import admin

from .models import Student

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display  = ('id','first_name','last_name','email', 'level', 'stream')


admin.site.register(model_or_iterable=Student,admin_class=StudentAdmin)
