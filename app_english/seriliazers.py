from django.middleware.security import SecurityMiddleware
from rest_framework import serializers

from .models import Answer, Cours, Exam, Option, Stream, Unit


class StreamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stream
        fields = ('name','level')

class UnitSerializer(serializers.ModelSerializer):

    stream_name = serializers.CharField(source='stream.name')
    class Meta:
        model = Unit
        fields = ("number","name","level","stream_name","description")


class CoursSerializer(serializers.ModelSerializer):
    stream_name = serializers.CharField(source='stream.name')
    unit_number = serializers.IntegerField(source="unit.number")
    unit_name = serializers.CharField(source='unit.name')
    class Meta:
        model = Cours
        fields = ("title","description","level","stream_name","unit_number","unit_name","format_cours","lesson")

class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = "__all__"


class OptionSerailizer(serializers.ModelSerializer):

    class Meta:
        model = Option
        fields = "__all__"

class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = "__all__"
