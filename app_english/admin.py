from django.contrib import admin

from .forms import UnitForm
from .models import Answer, Cours, Exam, Option, Question, Stream, Unit

# Register your models here.

class AllFieldsAdmin(admin.ModelAdmin):
    def __init__(self, model, admin_site):
        self.list_display = [
            field.name for field in model._meta.get_fields() if field.concrete
        ]
        super().__init__(model, admin_site)


class UnitAdmin(AllFieldsAdmin):
    form = UnitForm


admin.site.register(Unit, UnitAdmin)

for model in (Stream, Cours, Exam, Question, Option, Answer):
    admin.site.register(model, AllFieldsAdmin)
