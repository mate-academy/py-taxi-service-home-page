from datetime import datetime, timedelta

from django.shortcuts import render
from taxi.models import Driver, Manufacturer, Car


def timing():
    current_date = datetime.now()
    next_year_start = datetime(day=1, month=1, year=2023)
    time_delta = next_year_start - current_date
    return time_delta


def index(request):
    num_drivers = Driver.objects.count()
    num_manufacturers = Manufacturer.objects.count()
    num_cars = Car.objects.count()

    context = {
        "num_drivers": num_drivers,
        "num_manufacturers": num_manufacturers,
        "num_cars": num_cars,
        "before_new_year": timing(),

    }

    return render(request, "taxi/index.html", context=context)
