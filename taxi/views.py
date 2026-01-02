# taxi/views.py
from django.shortcuts import render
from .models import Manufacturer, Car, Driver


def index(request):
    """View function for the home page of the site."""

    # Count the number of objects
    num_drivers = Driver.objects.count()
    num_manufacturers = Manufacturer.objects.count()
    num_cars = Car.objects.count()

    # Pass the data to the template
    context = {
        "num_drivers": num_drivers,
        "num_manufacturers": num_manufacturers,
        "num_cars": num_cars,
    }

    # Render the HTML template index.html with the data in context
    return render(request, "taxi/index.html", context=context)
