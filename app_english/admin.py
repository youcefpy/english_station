from django.contrib import admin

from .models import Cours, Stream, Unit, Exam,Answer, Option, Question

# Register your models here.


class UnitAdmin(admin.ModelAdmin):
    class Meta: 
        model = Unit
        list_display = [field.name for field in Unit._meta.get_fields() if field.concrete]  # noqa: RUF012

class StreamAdmin(admin.ModelAdmin):
    class Meta:
        model = Stream
        list_display = [field.name for field in Stream._meta.get_fields() if field.concrete]  # noqa: RUF012


class CoursAdmin(admin.ModelAdmin):
    class Meta:
        model = Cours
        list_display = [field.name for field in Stream._meta.get_fields() if field.concrete]  # noqa: RUF012


class ExamAdmin(admin.ModelAdmin):
    class Meta:
        model = Exam
        list_display = [field.name for field in Stream._meta.get_fields() if field.concrete]  # noqa: RUF012

class QuestionAdmin(admin.ModelAdmin):
    class Meta:
        model = Question
        list_display = [field.name for field in Stream._meta.get_fields() if field.concrete]  # noqa: RUF012

class OptionAdmin(admin.ModelAdmin):
    class Meta:
        model = Option
        list_display = [field.name for field in Stream._meta.get_fields() if field.concrete]  # noqa: RUF012

class AnswerAdmin(admin.ModelAdmin):
    class Meta:
        model = Answer
        list_display = [field.name for field in Stream._meta.get_fields() if field.concrete]  # noqa: RUF012

admin.site.register(Unit,UnitAdmin)
admin.site.register(Stream,StreamAdmin)
admin.site.register(Cours,CoursAdmin)
admin.site.register(Exam,ExamAdmin)
admin.site.register(Question,QuestionAdmin)
admin.site.register(Option,OptionAdmin)
admin.site.register(Answer,AnswerAdmin)
