from django.db import models
from django.core.exceptions import ValidationError
from django.core import MinValueValidator, MaxValueValidator
from account.models import Student
from core.models import Department
from core.constants import SEMESTER_CHOICES, LEVEL_CHOICES


# Create your models here.

class AcademicSession(models.Model):
    name = models.CharField(max_length=20, help_text="e.g. 2024/2025")
    year = models.PositiveIntegerField(validators=[MinValueValidator(2000), MaxValueValidator(2100)])
    semester = models.IntegerField(max_length=10, choices=SEMESTER_CHOICES, default="first")
    is_current = models.BooleanField(default=False)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)



    class Meta:
        db_table = "academics_sessions"
        unique_together = (("year", "semester"),)
        ordering = ['-year', 'semester']


    def __str__(self):
        return f"{self.name} - {self.get_semester_display()}"



class Course(models.Model):
    department = models.ForeignKey(Department, on_delete=models.PROTECT, related_name="courses")
    code = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=200)
    credit_units = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(6)])
    level = models.CharField(max_length=3, choices=LEVEL_CHOICES, default="100")
    semester = models.CharField(max_length=10, choices=SEMESTER_CHOICES, default="first")
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = "academics_courses"
        ordering = ["code"]

    def __str__(self):
        return f"{self.code}: {self.title} ({self.credit_units} units)"



class CourseRegistration(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    register_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.course.title







