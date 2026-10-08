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
        cours = Cours.objects.get(pk=self.cours.pk)
        self.assertEqual(cours.title, "Introduction to Grammar")
        self.assertEqual(cours.unit, self.unit)
        self.assertEqual(cours.stream, self.stream)

    def test_stream_is_created(self):
        stream = Stream.objects.get(pk=self.stream.pk)
        self.assertEqual(stream.name, "English")
        self.assertEqual(stream.description, "English stream")
        self.assertEqual(stream.level, 1)

    def test_stream_can_be_updated(self):
        self.stream.name = "Advanced English"
        self.stream.save()
        self.stream.refresh_from_db()
        self.assertEqual(self.stream.name, "Advanced English")

    def test_stream_can_be_deleted(self):
        stream_id = self.stream.pk
        self.stream.delete()
        self.assertFalse(Stream.objects.filter(pk=stream_id).exists())

    def test_unit_is_created(self):
        unit = Unit.objects.get(pk=self.unit.pk)
        self.assertEqual(unit.name, "Grammar")
        self.assertEqual(unit.description, "Grammar lessons")

    def test_unit_can_be_updated(self):
        self.unit.name = "Advanced Grammar"
        self.unit.save()
        self.unit.refresh_from_db()
        self.assertEqual(self.unit.name, "Advanced Grammar")

    def test_unit_can_be_deleted(self):
        unit_id = self.unit.pk
        self.unit.delete()
        self.assertFalse(Unit.objects.filter(pk=unit_id).exists())

    def test_cours_can_be_updated(self):
        self.cours.title = "Advanced Grammar Course"
        self.cours.save()
        self.cours.refresh_from_db()
        self.assertEqual(self.cours.title, "Advanced Grammar Course")

    def test_cours_can_be_deleted(self):
        cours_id = self.cours.pk
        self.cours.delete()
        self.assertFalse(Cours.objects.filter(pk=cours_id).exists())


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

    def test_exam_can_be_updated(self):
        self.exam.title = "Advanced Grammar Exam"
        self.exam.save()
        self.exam.refresh_from_db()
        self.assertEqual(self.exam.title, "Advanced Grammar Exam")

    def test_exam_can_be_deleted(self):
        exam_id = self.exam.pk
        self.exam.delete()
        self.assertFalse(Exam.objects.filter(pk=exam_id).exists())
