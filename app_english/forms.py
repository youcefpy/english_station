from django import forms

from .models import Cours, Exam, Question, Stream, Unit


class StreamSelect(forms.Select):
    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        option = super().create_option(
            name, value, label, selected, index, subindex=subindex, attrs=attrs
        )
        if value:
            stream_level = Stream.objects.filter(
                pk=getattr(value, "value", value)
            ).values_list("level", flat=True).first()
            if stream_level is not None:
                option["attrs"]["data-level"] = str(stream_level)
        return option


class StreamForm(forms.ModelForm):
    class Meta:
        model = Stream
        fields = '__all__'  # noqa: DJ007

class CoursForm(forms.ModelForm):
    class Meta:
        model=Cours
        fields = '__all__'  # noqa: DJ007

class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = "__all__"  # noqa: DJ007
        widgets = {"stream": StreamSelect}

    class Media:
        js = ("app_english/unit_stream_filter.js",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        level = self.data.get(self.add_prefix("level"))
        if not level and self.instance.pk:
            level = self.instance.level
        if level:
            self.fields["stream"].queryset = Stream.objects.filter(level=level)

class ExamForm(forms.ModelForm):
    class Meta:
        model=Exam
        fields = '__all__'  # noqa: DJ007
class QuestionForm(forms.ModelForm):
    class Meta:
        model=Question
        fields="__all__"  # noqa: DJ007
