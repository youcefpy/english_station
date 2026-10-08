from django.test import TestCase

from app_english.models import Cours, Stream, Unit

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