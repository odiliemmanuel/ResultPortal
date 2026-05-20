from django.shortcuts import render
from .models import Department
from .serializers import DepartmentSerializer
# Create your views here.


def create_department(request):
