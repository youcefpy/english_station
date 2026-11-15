from rest_framework import serializers

from .models import Answer, Cours, Exam, Option, Stream, Unit


class StreamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stream
        fields = ('name','level')

class UnitSerializer(serializers.ModelSerializer):

    stream = StreamSerializer(many=True,read_only=True)
    class Meta:
        model = Unit
        fields = ("number","name","level","stream","description")


class CoursSerializer(serializers.ModelSerializer):
    stream = StreamSerializer(many=True, read_only=True)
    unit = UnitSerializer(many=True, read_only=True)
    class Meta:
        model = Cours
        fields = ("title","description","level","stream","unit","format_cours","lesson")

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
