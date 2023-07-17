
from taxi.models import Driver


def index(request):
    drivers = Driver.objects.count()
