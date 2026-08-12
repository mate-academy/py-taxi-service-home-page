from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from taxi.models import Car, Driver, Manufacturer


def index(request) -> HttpResponse:
    num_cars = Car.objects.count()
    num_drivers = Driver.objects.count()
    num_manufacturers = Manufacturer.objects.count()
    return render(
        request,
        "taxi/index.html",
        {
            "num_cars": num_cars,
            "num_drivers": num_drivers,
            "num_manufacturers": num_manufacturers,
        },
    )


class ManufacturerListView(ListView):
    model = Manufacturer


class CarListView(ListView):
    model = Car


class DriverListView(ListView):
    model = Driver


class ManufacturerDetailView(DetailView):
    model = Manufacturer


class CarDetailView(DetailView):
    model = Car


class DriverDetailView(DetailView):
    model = Driver
