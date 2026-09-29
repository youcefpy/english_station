from django.contrib import admin

from .models import Cours, Stream, Unit

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

admin.site.register(Unit,UnitAdmin)
admin.site.register(Stream,StreamAdmin)
admin.site.register(Cours,CoursAdmin)