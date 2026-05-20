from django.shortcuts import render
from rest_framework import status
from loguru import logger
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Department
from .serializers import DepartmentSerializer
# Create your views here.

@api_view(['POST'])
def create_department(request):
    try:
        serializer = DepartmentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        name = serializer.validated_data['name']
        logger.info(f"data validated for department {name}")


        Department.objects.create(**serializer.validated_data)
        logger.info(f"created department {name}")

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    except Exception as e:
        logger.error(f"Error creating department {str(e)}")