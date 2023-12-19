from django.db import models
from django.utils import timezone
from account_app.models import User

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=250, verbose_name="نام دوره")
    slug = models.SlugField()
    start_registration_date = models.DateTimeField()
    end_registration_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "دوره"
        verbose_name_plural = "دوره ها"


class Section(models.Model):
    title = models.CharField(max_length=250, verbose_name="نام بخش")
    slug = models.SlugField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "بخش"
        verbose_name_plural = "بخش ها"


class Exam(models.Model):
    title = models.CharField(max_length=250, verbose_name="امتحان")
    slug = models.SlugField()
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.section.title} - {self.title}"

    class Meta:
        verbose_name = "امتحان"
        verbose_name_plural = "امتحانات"

class RegisterCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="کاربر")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="درس")

    def __str__(self):
        return f"{self.user.first_name}{self.user.last_name} - {self.course}"

class Score(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="کاربر")
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, verbose_name="امتحان")
    score = models.IntegerField(verbose_name="نمره")

    def __str__(self):
        return f"{self.user.first_name}{self.user.last_name} - {self.exam.title} - {self.score}"
