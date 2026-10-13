from django.conf import settings
from django.core.validators import (
    FileExtensionValidator,
    MaxValueValidator,
    MinValueValidator,
)
from django.db import models

from utils import AcadimicLevelChoices, StreamNameChoices, lesson_upload_path

# Create your models here.

class Stream(models.Model):
    name = models.CharField(
        max_length=50,
        choices=StreamNameChoices.choices,
        unique=True,
    )
    level = models.IntegerField(choices=AcadimicLevelChoices)

    def __str__(self):
        return f"{self.level}-{self.name}"
class Unit(models.Model):
    number = models.PositiveIntegerField(unique=False)
    name=  models.CharField(max_length=255)
    level = models.IntegerField(choices=AcadimicLevelChoices)
    stream = models.ForeignKey(Stream,on_delete=models.CASCADE)
    description = models.TextField()
    class Meta:
        ordering  = ["number"]  # noqa: RUF012

    def __str__(self):
        return f"{self.name}"

class Cours(models.Model):
    class FormatCours(models.TextChoices):
        WORD = "WORD", ".docx"
        PDF = "PDF", ".pdf"
        TXT = "TXT", ".txt"
        MP4 = "MP4", ".mp4"
        WEBM = "WEBM", ".webm"
        MOV = "MOV", ".mov"
        PNG = "PNG", ".png"
        JPEG= "JPEG", ".jpeg"

    title = models.CharField(max_length=255)
    description = models.TextField()
    level = models.IntegerField(choices=AcadimicLevelChoices)
    stream = models.ForeignKey(Stream,on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit,on_delete=models.CASCADE)
    format_cours = models.CharField(choices=FormatCours,default=FormatCours.PDF)
    lesson = models.FileField(upload_to=lesson_upload_path,
        validators=[
            FileExtensionValidator(
                allowed_extensions=['pdf', 'doc', 'docx', 'txt',
                                    'mp4', 'mkv', 'avi', 'mov', 'png','jpeg']
            )
        ]
    )
    def __str__(self):
        return f"{self.stream.name}: {self.unit.name} : {self.title}"
class Exam(models.Model):
    title = models.CharField(max_length=255)
    cours = models.OneToOneField(Cours,on_delete=models.CASCADE)
    passing_scrore = models.IntegerField(
        default=0,
        validators=[MinValueValidator(1), MaxValueValidator(10)]
        )

    def __str__(self):
        return f"{self.title}"

class Question(models.Model):
    exam = models.ForeignKey(Exam, related_name="questions", on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    allow_multiple = models.BooleanField(
        default=False, help_text="Tick to let users pick several options"
    )
    def __str__(self):
        return self.text
class Option(models.Model):
    question = models.ForeignKey(Question, related_name="options",
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    score = models.IntegerField(
        default=0,
        help_text=
        "Points earned if selected. 0 = wrong answer "
        "(use a negative value to penalise)",
    )
    class Meta:
        unique_together = ("question", "name")

    def __str__(self) -> str:
        return self.name

    @property
    def is_correct(self):
        return self.score > 0

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    selected = models.ManyToManyField(Option)  # holds 1 item or several
    score = models.IntegerField(default=0)  # saved at submission time

    def __str__(self):
        return f"{self.question}"

    def compute_score(self):
        total = self.selected.aggregate(total=models.Sum("score"))["total"] or 0
        return max(total, 0)  # remove max() if you allow negative totals

