from django.urls import path
from .views import health, totals

urlpatterns = [
    path("health/", health, name="api-health"),
    path("totals/", totals, name="api-totals"),
]
