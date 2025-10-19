from django.contrib import admin
from django.urls import path, include
from dashboards.views import home as dashboard_home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", dashboard_home, name="home"),
    path("api/", include("api.urls")),
]
