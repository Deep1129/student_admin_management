from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views  # Import Django's built-in login/logout views
from erp.views import teacher_dashboard  # Import the teacher dashboard view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('erp/', include('erp.urls')),  # Keep ERP app URLs

    # ✅ Teacher Login & Logout URLs
    path('teacher/login/', auth_views.LoginView.as_view(template_name="erp/teacher_login.html"), name="teacher_login"),
    path('teacher/logout/', auth_views.LogoutView.as_view(next_page="/teacher/login/"), name="teacher_logout"),

    # ✅ Fix: Add teacher dashboard URL
    path('teacher/dashboard/', teacher_dashboard, name='teacher_dashboard'),
]
