from django.urls import path
from . import views

app_name = "profile"

urlpatterns = [
    path('dashboard', views.ProfileView.as_view(), name="dashboard"),
    path('my-courses', views.MyCourses.as_view(), name="my-courses"),
    path('courses-list', views.CourseList.as_view(), name="courses-list"),
    path('register/<pk>', views.register, name="register"),
    path('karname', views.karname_page, name="karname"),
    path('download/<id>', views.download_karname, name="download"),
    path('handel/<id>', views.handel_proceess_of_karname, name="handel"),
    path('logout', views.LogOutView.as_view(), name="logout"),
]