from rest_framework import serializers


class CourseSerializer(serializers.Serializer):
    department_id = serializers.IntegerField(required=True)
    code = serializers.CharField(max_length=20,required=True)
    title = serializers.CharField(max_length=200, required=True)
    credit_units = serializers.IntegerField(required=True)
    level = serializers.CharField(required=True)
    semester = serializers.CharField(required=True)
    description = serializers.CharField(required=False, allow_blank=True)