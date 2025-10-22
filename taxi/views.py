from django.contrib.auth import get_user_model
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from taxi.models import Manufacturer, Car


def index(request: HttpRequest) -> HttpResponse:
    return render(
        request=request,
        template_name="taxi/index.html",
        context={
            "num_drivers": get_user_model().objects.count(),
            "num_manufacturers": Manufacturer.objects.count(),
            "num_cars": Car.objects.count()
        }

    )
