import json
import os

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from collections import Counter


def index(request: HttpRequest) -> HttpResponse:
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, "taxi_service_db_data.json")
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            data = json.load(file)

        models_counter = Counter(item["model"] for item in data)
        num_drivers = models_counter["taxi.driver"]
        num_manufacturers = models_counter["taxi.manufacturer"]
        num_cars = models_counter["taxi.car"]

        context = {
            "num_cars": num_cars,
            "num_drivers": num_drivers,
            "num_manufacturers": num_manufacturers,
        }

    return render(request, "taxi/index.html", context=context)
