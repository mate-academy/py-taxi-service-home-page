from django.shortcuts import render
from django.http import HttpResponse
from taxi.models import Driver, Manufacturer, Car


def index(request):
    contex = {
        "num_drivers": Driver.objects.all().count(),
        "num_manufacturers": Manufacturer.objects.all().count(),
        "num_cars": Car.objects.all().count()
    }

    return render(request, "taxi/index.html", context=contex)
