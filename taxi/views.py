from django.http import HttpResponse
from django.shortcuts import render

from taxi.models import Driver, Manufacturer, Car


def index(request):
    number_of_all_drivers = Driver.objects.count()
    number_of_all_manufacturers = Manufacturer.objects.count()
    number_of_all_cars = Car.objects.count()

    context = {
        "number_of_all_drivers": number_of_all_drivers,
        "number_of_all_manufacturers": number_of_all_manufacturers,
        "number_of_all_cars": number_of_all_cars,
    }

    return render(request=request,
                  template_name="taxi/index.html",
                  context=context)
