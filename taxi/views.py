from django.http import HttpResponse
from django.template import loader

from taxi.models import Driver, Manufacturer, Car


# Create your views here.
def index(request) -> HttpResponse:
    num_drivers = Driver.objects.count()
    num_manufacturers = Manufacturer.objects.count()
    num_cars = Car.objects.count()

    template = loader.get_template('taxi/index.html')
    context = {
        "num_drivers": num_drivers,
        "num_manufacturers": num_manufacturers,
        "num_cars": num_cars,
    }

    return HttpResponse(template.render(context, request))
