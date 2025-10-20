from django.contrib import admin
from django.urls import path, include


from dashboards.views import admin_dashboard

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", admin_dashboard, name="home"),
    path("api/", include("api.urls")),
    path("dashboards/", include("dashboards.urls")),
    path("students/", include("students.urls")),
    path("schedulemaster/", include("backend.schedulemaster.urls")),
]
