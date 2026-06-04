from rest_framework.viewsets import ModelViewSet
from .models import Course, AcademicSession
from .serializers import CourseSerializer, AcademicsSessionSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_queryset(self):
        Course.objects.filter(course_id=self.kwargs['nested_1_ok'])

    def get_serializer_context(self):
        return {"department_id": self.kwargs.get("nested_1_pk")}


class AcademicSessionViewSet(ModelViewSet):
    queryset = AcademicSession.objects.all()

    def get_serializer_class(self):

        if self.request.method == "POST":
            return AcademicsSessionSerializer
        return None