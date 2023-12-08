from django.shortcuts import render

from .models import Driver, Manufacturer, Car

app_name = "taxi"


def index(request):  # 3
    context = {
        "num_drivers": Driver.objects.count(),
        "num_manufacturers": Manufacturer.objects.count(),
        "num_cars": Car.objects.count(),
    }

    return render(request, template_name="base.html", context=context)
