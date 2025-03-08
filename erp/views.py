from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .forms import AttendanceForm
from .models import Attendance, Teacher  # Import Teacher model

# Helper function to ensure the user is a teacher (staff)
def staff_required(user):
    return user.is_staff and hasattr(user, 'teacher')  # Ensure user is a teacher

# Teacher Dashboard View
@login_required
@user_passes_test(staff_required)
def teacher_dashboard(request):
    teacher_name = request.user.get_full_name() or request.user.username  # Get teacher's name
    return render(request, 'erp/teacher_dashboard.html', {'teacher_name': teacher_name})

# Add Attendance View
@login_required
@user_passes_test(staff_required)
def add_attendance(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            attendance = form.save(commit=False)
            attendance.teacher = request.user.teacher  # Assign teacher who marked attendance
            attendance.save()  # Save the new attendance record
            messages.success(request, "Attendance recorded successfully!")
            return redirect('attendance_list')  # Redirect to list view after saving
        else:
            messages.error(request, "There was an error submitting the form.")
    else:
        form = AttendanceForm()
    return render(request, 'erp/add_attendance.html', {'form': form})

# Attendance List View (Only Show Attendance Marked by This Teacher)
@login_required
@user_passes_test(staff_required)
def attendance_list(request):
    teacher = request.user.teacher  # Get the logged-in teacher
    records = Attendance.objects.filter(teacher=teacher).order_by('-date')  # Filter by teacher
    return render(request, 'erp/attendance_list.html', {'records': records})
