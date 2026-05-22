from .views import create_course
from django.urls import path


urlpatterns = [
    path('create-course/', create_course, name='create-course'),
]