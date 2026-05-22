from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from loguru import logger
from .models import Department
from .serializers import DepartmentSerializer


@api_view(['POST'])
def create_department(request):
    try:
        serializer = DepartmentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        name = serializer.validated_data['name']
        code = serializer.validated_data['code']
        logger.info(f"data validated for department: {name}")

        if Department.objects.filter(code=code).exists():
            logger.error(f"department with {code} already exists")
            return Response({"message": "department with code already exists"},
                            status=status.HTTP_400_BAD_REQUEST)

        Department.objects.create(**serializer.validated_data)
        logger.info(f"department {name} created")

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as e:
        logger.error(f"Error creating department: {str(e)}")
        return Response({"message": "Error creating department"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




@api_view(['GET'])
def get_department(request, code):
    department = get_object_or_404(Department, code=code, is_active=True)
    serializer = DepartmentSerializer(department)
    logger.info(f"department {code} retrieved")
    return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(['PUT', 'PATCH'])
def update_department(request, code):
    department = get_object_or_404(Department, code=code)
    try:
        serializer = DepartmentSerializer(department, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        logger.info(f"department {department.name} updated")
        return Response(serializer.data, status=status.HTTP_200_OK)

    except ValueError as e:
        logger.error(f"Error validation department: {str(e)}")
        return Response({"message": "Error validation department"}, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        logger.error(f"Error updating department: {str(e)} ")
        return Response({"message": "Error updating department"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_department(request, code):
    department = get_object_or_404(Department, code=code)
    department.is_active = False
    department.save()
    logger.info(f"department {code} deleted")
    return Response(status=status.HTTP_204_NO_CONTENT)