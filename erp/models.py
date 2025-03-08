from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone  # ✅ Import timezone for default date value

class Teacher(models.Model):
    """Model for Teachers, linked to the Django User model."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Deletes teacher if User is deleted
    subject = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.subject or 'No Subject'}"

class Student(models.Model):
    """Model for Students, linked to the Django User model."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Deletes student if User is deleted
    enrollment_number = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.user.username} ({self.enrollment_number})"

class Attendance(models.Model):
    """Attendance model linking students to teachers for each date."""
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True, blank=True)  # ✅ Ensures attendance is deleted if the teacher is removed
    student = models.ForeignKey(Student, on_delete=models.CASCADE)  # ✅ Ensures attendance is deleted if the student is removed
    date = models.DateField(default=timezone.now)  # ✅ Allows editing but auto-fills the current date
    present = models.BooleanField(default=True)  # ✅ Boolean to store presence status

    def __str__(self):
        status = "Present" if self.present else "Absent"
        teacher_info = self.teacher.subject if self.teacher else "No Teacher Assigned"
        return f"{self.student.user.username} - {teacher_info} - {self.date} - {status}"
