
from rest_framework import serializers


class StudentEnrollmentSerializer(serializers.Serializer):
    department = serializers.CharField(max_length=10, required=True)
    entry_year = serializers.IntegerField()
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)



class StaffEnrollmentSerializer(serializers.Serializer):
    department = serializers.CharField(max_length=10, required=True)
    designation = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)


    {
        "department": "EE101",
        "entry_year": 2026,
        "email": "odiliejeh09@gmail.com",
        "username": "Odils",
        "password": "9087",
        "first_name": " Kaodilichi",
        "last_name": "Ejeh"
    }