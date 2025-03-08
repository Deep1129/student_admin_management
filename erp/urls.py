from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('attendance/add/', views.add_attendance, name='add_attendance'),
    path('attendance/list/', views.attendance_list, name='attendance_list'),
    path('teacher/dashboard/', views.teacher_dashboard, name='teacher_dashboard'),

    # Teacher Login & Logout URLs
    path('teacher/login/', auth_views.LoginView.as_view(template_name='erp/teacher_login.html'), name='teacher_login'),
    path('teacher/logout/', auth_views.LogoutView.as_view(next_page='teacher_login'), name='teacher_logout'),
]
