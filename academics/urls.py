from django.urls import path, include
from rest_framework import routers

from academics.views import AcademicSessionViewSet

router = routers.DefaultRouter()
router.register('', AcademicSessionViewSet, basename='academic-sessions')

urlpatterns = [
    path('', include(router.urls)),
]