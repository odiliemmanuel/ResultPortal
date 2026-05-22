
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from loguru import logger

from core.models import Department
from academics.models import Course
from academics.serializers import CourseSerializer


@api_view(['POST'])
def create_course(request):
    try:
        serializer = CourseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        department_id = serializer.validated_data['department_id']

        try:
            department = Department.objects.get(id=department_id)
        except Department.DoesNotExist:
            logger.error(f"Department with id {department_id} does not exist")
            return Response({"message": "department does not exist"}, status=status.HTTP_404_NOT_FOUND)

        code = serializer.validated_data['code']

        if Course.objects.filter(code=code).exists():
            logger.error(f"Course with code {code} already exists")
            return Response({"message": "Course with code already exists"}, status=status.HTTP_409_CONFLICT)

        course = Course.objects.create(
            department=department,
            code=serializer.validated_data['code'],
            title = serializer.validated_data['title'],
            credit_units = serializer.validated_data['credit_units'],
            level = serializer.validated_data['level'],
            semester = serializer.validated_data['semester'],
            description = serializer.validated_data['description']
        )

        logger.info(f"Course with code {course.code} created")
        return Response({
            "message": "Course created successfully",
            "data": {
                "id": course.id,
                "code": course.code,
                "title": course.title,
            }
        }, status=status.HTTP_201_CREATED)
    except Exception as e:
        logger.error(f"Error creating course: {str(e)}")
        return Response({"message": "Error creating course"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)