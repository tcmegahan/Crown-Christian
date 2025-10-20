from django.urls import path
from . import views

urlpatterns = [
	path("admin/", views.admin_dashboard, name="admin_dashboard"),
	path("staff_dashboard/", views.staff_dashboard, name="staff_dashboard"),
	path("teacher_dashboard/", views.teacher_dashboard, name="teacher_dashboard"),
]
