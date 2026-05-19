from django.db import models

from core.models import User, Department


class Student(models.Model):
    class Level(models.TextChoices):
        LEVEL100 = "Level 100"
        LEVEL200 = "Level 200"
        Level300 = "Level 300"
        Level400 = "Level 400"
        Level500 = "Level 500"


    class Status(models.TextChoices):
        ACTIVE = "Active"
        INACTIVE = "Inactive"
        SUSPENDED = "Suspended"
        WITHDRAWN = "Withdrawn"


    level = models.CharField(max_length=20, choices=Level, default=Level.LEVEL100)
    status = models.CharField(max_length=20, choices=Status, default=Status.ACTIVE)
    matric_number = models.CharField(max_length=20, unique=True, default="")
    enrolled_at = models.DateField(null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.matric_number
    

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    designation = models.CharField(max_length=55, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f" {self.user} - {self.designation}"

    class Meta:
        ordering = ['designation']

