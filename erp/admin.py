from django.contrib import admin
from .models import Subject, Teacher, Student, Attendance  # Import Subject model

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Display subject names in admin

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_subjects')  # Use a function to display subjects
    search_fields = ('user__username',)  # Search by username only
    filter_horizontal = ('subjects',)  # Use filter_horizontal for ManyToManyField

    def get_subjects(self, obj):
        """Returns a comma-separated string of subjects assigned to a teacher."""
        return ", ".join(subject.name for subject in obj.subjects.all())
    get_subjects.short_description = "Subjects"  # Custom column name in admin panel

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'enrollment_number')  # Display username and enrollment number
    search_fields = ('user__username', 'enrollment_number')  # Allow searching
    list_filter = ('enrollment_number',)  # Filter students by enrollment number

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'teacher', 'subject', 'date', 'present')  # Include subject
    list_filter = ('date', 'present', 'subject')  # Allow filtering by subject
    search_fields = ('student__user__username', 'teacher__user__username')  # Search by student and teacher usernames
    ordering = ('-date',)  # Show latest attendance records first
