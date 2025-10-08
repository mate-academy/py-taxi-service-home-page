from django.shortcuts import render
from django.views.generic import ListView
from .models import Manufacturer, Driver, Car


# --- FUNKCJA INDEX (DASHBOARD) ---
def index(request):
    """View function for the home page of the site."""

    # Liczenie obiektów z bazy danych
    num_cars = Car.objects.count()
    num_drivers = Driver.objects.count()
    num_manufacturers = Manufacturer.objects.count()

    context = {
        "num_cars": num_cars,
        "num_drivers": num_drivers,
        "num_manufacturers": num_manufacturers,
    }

    # Renderowanie szablonu index.html z danymi kontekstowymi
    return render(request, "taxi/index.html", context=context)


# --- KLASA LISTY PRODUCENTÓW ---
class ManufacturerListView(ListView):
    model = Manufacturer
    template_name = "taxi/manufacturer_list.html"
    context_object_name = "manufacturer_list"
