from django.shortcuts import render

from django.shortcuts import render

from .models import Manufacturer, Driver, Car


def index(request):
    context = {
        "num_drivers": Driver.objects.count(),
        "num_manufacturers": Manufacturer.objects.count(),
        "num_cars": Car.objects.count(),
    }
    return render(request, 'taxi/index.html', context=context)
