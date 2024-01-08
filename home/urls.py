from django.urls import path
from . import views
app_name = 'home'

urlpatterns = [
    path("", views.Hoem.as_view(), name="home")
]