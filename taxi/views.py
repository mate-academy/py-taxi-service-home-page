from datetime import datetime, timedelta

from django.shortcuts import render
from taxi.models import Driver, Manufacturer, Car


def timing():
    current_date = datetime.now()
    next_year_start = datetime(day=1, month=1, year=2023)
    return next_year_start - current_date


def index(request):
    context = {
        "num_drivers": Driver.objects.count(),
        "num_manufacturers": Manufacturer.objects.count(),
        "num_cars": Car.objects.count(),
        "before_new_year": timing(),
    }
    return render(request, "taxi/index.html", context=context)
