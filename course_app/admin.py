from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Course)
admin.site.register(Section)
admin.site.register(Exam)
admin.site.register(RegisterCourse)
admin.site.register(Score)