from base.models.named_model import NamedModel
from django.db import models

class ProviderModel(NamedModel):
    first_name = models.CharField(max_length=100)
    number = models.CharField(max_length=10)
    address = models.CharField(max_length=255)