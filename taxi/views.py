from django.shortcuts import render
from .models import Driver, Manufacturer, Car

# Create your views here.


def index(request):
    context = {
        "num_drivers": Driver.objects.count(),
        "num_manufacturers": Manufacturer.objects.count(),
        "num_cars": Car.objects.count(),
    }

    return render(request, "taxi/index.html", context=context)
