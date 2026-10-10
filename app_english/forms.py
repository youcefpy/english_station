from django import forms

from .models import AcadimicLevelChoices, Cours, Exam, Question, Stream, Unit


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


class UnitSelect(forms.Select):
    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        option = super().create_option(
            name, value, label, selected, index, subindex=subindex, attrs=attrs
        )
        if value:
            unit = Unit.objects.filter(
                pk=getattr(value, "value", value)
            ).values("level", "stream_id").first()
            if unit:
                option["attrs"]["data-level"] = str(unit["level"])
                option["attrs"]["data-stream"] = str(unit["stream_id"])
        return option


class StreamForm(forms.ModelForm):
    class Meta:
        model = Stream
        fields = '__all__'  # noqa: DJ007

class CoursForm(forms.ModelForm):
    level = forms.ChoiceField(choices=AcadimicLevelChoices.choices)
    stream = forms.ModelChoiceField(
        queryset=Stream.objects.all(), widget=StreamSelect
    )

    class Meta:
        model=Cours
        fields = ("title", "description", "level", "stream", "unit", "format_cours", "lesson")
        widgets = {"stream": StreamSelect, "unit": UnitSelect}

    class Media:
        js = ("app_english/unit_stream_filter.js",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        level = self.data.get(self.add_prefix("level"))
        stream_id = self.data.get(self.add_prefix("stream"))

        if not level and self.instance.pk:
            level = self.instance.unit.level
        if not stream_id and self.instance.pk:
            stream_id = self.instance.unit.stream_id

        if level:
            self.fields["stream"].queryset = Stream.objects.filter(level=level)
            self.fields["unit"].queryset = Unit.objects.filter(level=level)
        if stream_id:
            self.fields["unit"].queryset = self.fields["unit"].queryset.filter(
                stream_id=stream_id
            )

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
