from django.test import TestCase

from django.urls import reverse
from django.test import Client, TestCase

class DashboardsTest(TestCase):
    def test_dashboard_home_view(self):
        client = Client()
        response = client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
