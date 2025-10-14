from django.shortcuts import render
from .models import Driver, Car, Manufacturer
from django.http import HttpResponse, HttpRequest


def index(request: HttpRequest) -> HttpResponse:
    num_drivers = Driver.objects.all()
    num_manufacturers = Manufacturer.objects.all()
    num_cars = Car.objects.all()
    return HttpResponse("Hello, world!")

