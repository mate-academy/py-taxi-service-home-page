from django.http import HttpResponse
from django.shortcuts import render

from .models import *

print("taxi/views")

app_name = "taxi"


def index(request):
    context = {
        "num_drivers": Driver.objects.count(),
        "num_manufacturers": Manufacturer.objects.count(),  # 3
        "num_cars": Car.objects.count(),
    }

    return render(request, template_name="base.html", context=context)
