from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser



class User(AbstractBaseUser):
    class Role(models.TextChoices):
        ADMIN = 'admin', 'Admin'
        USER = 'user', 'User'
        STUDENT = 'student', 'Student'

    first_name = models.CharField(max_length=250, blank=False, null=False)
    last_name = models.CharField(max_length=250, blank=False, null=False)
    email = models.EmailField(max_length=250, unique=True, blank=False, null=False)
    username = models.CharField(max_length=250, unique=True, blank=False, null=False)
    password = models.CharField(max_length=250, blank=False, null=False)
    role = models.CharField(max_length=10, choices=Role, default=Role.STUDENT)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class Department(models.Model):
    name = models.CharField(max_length=250, blank=False, null=False)
    code = models.CharField(max_length=10, unique=True, blank=False, null=False)
    description = models.CharField(max_length=250, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.name} {self.code}"

