from django.test import TestCase
from django.urls import reverse

from taxi.models import Manufacturer, Driver, Car


class HomeTestPage(TestCase):
    def setUp(self):
        for _ in range(5):
            Driver.objects.create(username="test" + str(_),
                                  license_number=str(_))
        for _ in range(10):
            Car.objects.create(model="test", manufacturer_id=1)
        for _ in range(16):
            Manufacturer.objects.create(name="test" + str(_))

    def test_context_data(self):
        url = reverse("taxi:index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["num_drivers"], Driver.objects.count())
        self.assertEqual(response.context["num_manufacturers"], Manufacturer.objects.count())
        self.assertEqual(response.context["num_cars"], Car.objects.count())
