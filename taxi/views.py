from django.shortcuts import render
from taxi.models import Driver, Manufacturer, Car


def index(request):
    context = {
        "num_drivers": Driver.objects.count(),
        "num_manufacturers": Manufacturer.objects.count(),
        "num_cars": Car.objects.count()
    }
    print(context)
    return render(request, "taxi/index.html", context=context)
