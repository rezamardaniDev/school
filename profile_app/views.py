from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.views.generic import *
from .forms import *
from .utility import process
from course_app.models import RegisterCourse, Course,Score, Section


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

def karname_page(request):
    courses = RegisterCourse.objects.filter(user_id=request.user.id).all()
    print(courses)
    return render(request, 'karname.html', context={
        'courses': courses
    })

def download_karname(request, id):
    section = Section.objects.filter(course_id=id).all()
    print(section)
    return render(request, 'part.html', context={
        'sections': section
    })

def handel_proceess_of_karname(request, id):
    scores = Score.objects.filter(exam__section_id=id, user_id=request.user.id).all()
    title = []
    score = []
    for item in scores:
        title.append(item.exam.title)
        score.append(item.score)
    print(title, score)
    process.accepted(title, score, request.user.username)
    return render(request, 'part.html', context={})

class LogOutView(View):
    def get(self, request):
        logout(request)
        return redirect("home:home")