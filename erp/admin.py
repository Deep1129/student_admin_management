from django.contrib import admin
from .models import Teacher, Student, Attendance  # ✅ Import all models

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user', 'subject')  # Display these fields in the list view
    search_fields = ('user__username', 'subject')  # Allow searching by username and subject
    list_filter = ('subject',)  # Filter teachers by subject

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'enrollment_number')  # Display username and enrollment number
    search_fields = ('user__username', 'enrollment_number')  # Search by username or enrollment number
    list_filter = ('enrollment_number',)  # Filter students by enrollment

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'teacher', 'date', 'present')  # Display these fields in admin
    list_filter = ('date', 'present')  # Allow filtering by date and presence status
    search_fields = ('student__user__username', 'teacher__user__username')  # Search by student and teacher usernames
    ordering = ('-date',)  # Show latest attendance records first
