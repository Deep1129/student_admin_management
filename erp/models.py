from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone  # Import timezone for default date values

#  Subject Model       
class Subject(models.Model):
    """Model to store different subjects like Math, Science, etc."""
    name = models.CharField(max_length=100, unique=True)  # Ensures subject names are unique

    def __str__(self):
        return self.name  # Displays subject name in Django admin & shell


#  Teacher Model             

class Teacher(models.Model):
    """Model for Teachers, linked to the Django User model."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Deletes teacher if User is deleted
    subjects = models.ManyToManyField(Subject, blank=True)  # Many-to-Many → A teacher can have multiple subjects

    def __str__(self):
        # Returns username + subjects assigned
        subject_names = ', '.join([s.name for s in self.subjects.all()]) if self.subjects.exists() else "No Subject"
        return f"{self.user.username} - {subject_names}"

#  Student Model 
            
class Student(models.Model):
    """Model for Students, linked to the Django User model."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Deletes student if User is deleted
    enrollment_number = models.CharField(max_length=20, unique=True)  # Unique ID for each student

    def __str__(self):
        return f"{self.user.username} ({self.enrollment_number})"  # Shows username & enrollment number

# Attendance Model 
         
class Attendance(models.Model):
    """Model to store attendance records, linking students to teachers & subjects."""
    
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True, blank=True)  
    #  Teacher marking attendance (Can be NULL for now, but should be assigned)

    student = models.ForeignKey(Student, on_delete=models.CASCADE)  
    #  The student whose attendance is being marked

    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, blank=True)
    #  Subject for which attendance is being marked

    date = models.DateField(default=timezone.now)  
    #  Auto-fills with current date (but allows editing)

    present = models.BooleanField(default=True)  
    #  Stores whether the student is present or absent

    def __str__(self):
        """Returns a readable string format for Attendance"""
        status = "Present" if self.present else "Absent"
        teacher_info = f"{self.teacher.user.username} ({', '.join([s.name for s in self.teacher.subjects.all()])})" if self.teacher else "No Teacher Assigned"
        subject_name = self.subject.name if self.subject else "No Subject"
        return f"{self.student.user.username} - {teacher_info} - {subject_name} - {self.date} - {status}"
