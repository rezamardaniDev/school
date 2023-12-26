from django.shortcuts import render, redirect
from django.views.generic import *
from .forms import *
from course_app.models import RegisterCourse, Course,Score


# Create your views here.
class ProfileView(View):
    def get(self, request):
        return render(request, 'profile.html', context={

        })

class MyCourses(View):
   def get(self, request):
       courses:RegisterCourse = RegisterCourse.objects.filter(user_id=request.user.id).all()
       return render(request, 'my_courses.html', context={
           "mycourse": courses
       })

class CourseList(View):
    def get(self, request):
        courses = Course.objects.all()
        registered_courses = RegisterCourse.objects.filter(user=request.user).values_list('course_id', flat=True)
        return render(request, 'register_course.html', context={
            "courses": courses,
            'registered_courses': registered_courses
        })

def register(request, pk):
    new_register = RegisterCourse()
    new_register.user = request.user
    new_register.course_id = pk
    new_register.save()
    return redirect('profile:my-courses')

def karname(request, course_slug):
    karname = Score.objects.filter(user=request.user, exam__section__course__slug=course_slug)
    return render(request, 'karname.html', context={
        'karnmae': karname
    })