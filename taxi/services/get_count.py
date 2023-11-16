from typing import Type

from django.db.models import Model


def get_objects_count(model: Model | Type) -> int:
    return model.objects.count()
