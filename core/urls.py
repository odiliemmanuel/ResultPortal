from core.views import create_department, update_department, get_department, delete_department
from django.urls import path

urlpatterns = [
    path('create/', create_department, name='create-department'),
    path('get/<str:code>/', get_department, name='get-department'),
    path('update/<str:code>/', update_department, name='update-department'),
    path('delete/<str:code>/', delete_department, name='delete-department'),
]