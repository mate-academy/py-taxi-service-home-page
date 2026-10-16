from django.contrib.auth import get_user_model
from django.contrib.staticfiles import finders
from django.test import TestCase
from django.urls import resolve, reverse

from taxi.models import Car, Manufacturer


class IndexTests(TestCase):
    fixtures = []

    def test_root_uses_namespaced_home_page(self):
        self.assertEqual(reverse("taxi:index"), "/")
        self.assertEqual(resolve("/").view_name, "taxi:index")

    def test_empty_service_renders_zero_counts_and_shared_templates(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        for key in ("num_cars", "num_drivers", "num_manufacturers"):
            self.assertEqual(response.context[key], 0)
        for template in (
            "taxi/index.html", "base.html", "includes/sidebar.html"
        ):
            self.assertTemplateUsed(response, template)
        for label in ("Home page", "Manufacturers", "Cars", "Drivers"):
            self.assertContains(response, label)
        self.assertContains(response, "/static/css/styles.css")

    def test_totals_include_records_without_assigned_drivers(self):
        manufacturer = Manufacturer.objects.create(
            name="Toyota", country="Japan"
        )
        Car.objects.create(model="Prius", manufacturer=manufacturer)
        get_user_model().objects.create_user(
            username="driver", license_number="ABC12345"
        )
        response = self.client.get("/")
        self.assertEqual(response.context["num_cars"], 1)
        self.assertEqual(response.context["num_drivers"], 1)
        self.assertEqual(response.context["num_manufacturers"], 1)
        Car.objects.create(model="Corolla", manufacturer=manufacturer)
        self.assertEqual(self.client.get("/").context["num_cars"], 2)

    def test_project_stylesheet_can_be_found(self):
        self.assertIsNotNone(finders.find("css/styles.css"))
