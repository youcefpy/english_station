from django.test import TestCase

from app_english.models import Cours, Exam, Stream, Unit

# Create your tests here.


class CoursTestCase(TestCase):
    def setUp(self):
        self.stream = Stream.objects.create(
            name="English",
            description="English stream",
            level=1,
        )
        self.unit = Unit.objects.create(
            name="Grammar",
            description="Grammar lessons",
        )
        self.cours = Cours.objects.create(
            title="Introduction to Grammar",
            description="An introductory grammar lesson",
            unit=self.unit,
            stream=self.stream,
        )

    def test_cours_is_created(self):
        self.assertEqual(self.cours.title, "Introduction to Grammar")
        self.assertEqual(self.cours.unit, self.unit)
        self.assertEqual(self.cours.stream, self.stream)

    def test_stream_is_created(self):
        stream = Stream.objects.get(pk=self.stream.pk)
        self.assertEqual(stream.name, "English")
        self.assertEqual(stream.description, "English stream")
        self.assertEqual(stream.level, 1)

    def test_unit_is_created(self):
        unit = Unit.objects.get(pk=self.unit.pk)
        self.assertEqual(unit.name, "Grammar")
        self.assertEqual(unit.description, "Grammar lessons")


class ExamTestCase(TestCase):
    def setUp(self):
        stream = Stream.objects.create(
            name="English",
            description="English stream",
            level=1,
        )
        unit = Unit.objects.create(
            name="Grammar",
            description="Grammar lessons",
        )
        cours = Cours.objects.create(
            title="Introduction to Grammar",
            description="An introductory grammar lesson",
            unit=unit,
            stream=stream,
        )
        self.exam = Exam.objects.create(
            title="Grammar Exam",
            cours=cours,
        )

    def test_exam_is_created(self):
        exam = Exam.objects.get(pk=self.exam.pk)
        self.assertEqual(exam.title, "Grammar Exam")
        self.assertEqual(exam.cours.title, "Introduction to Grammar")
