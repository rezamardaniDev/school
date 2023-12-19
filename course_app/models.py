from django.db import models
from django.utils import timezone


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
        return self.title

    class Meta:
        verbose_name = "امتحان"
        verbose_name_plural = "امتحانات"
