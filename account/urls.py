from django.urls import path, include
from . import views

urlpatterns = [
    path('student-enroll/', views.StudentEnrollment.as_view(), name='student-enroll'),
    path('staff-enroll/', views.StaffEnrollment.as_view(), name='staff-enroll'),

]