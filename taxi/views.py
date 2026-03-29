from taxi.models import Car, Manufacturer, Driver

from django.shortcuts import render


def index(request):
    context = {
        "num_drivers": Driver.objects.count(),
        "num_manufacturers": Manufacturer.objects.count(),
        "num_cars": Car.objects.count(),
    }

    return render(
        request=request,
        template_name="taxi/index.html",
        context=context,
    )
