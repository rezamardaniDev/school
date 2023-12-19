from django import forms

from course_app.models import RegisterCourse


class RegisterCourseForm(forms.ModelForm):
    class Meta:
        model = RegisterCourse
        fields = "__all__"