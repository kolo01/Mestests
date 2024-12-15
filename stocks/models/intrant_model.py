from base.models.labelled_model import LabelledModel
from django.db import models

class IntrantModel(LabelledModel):
    quantity = models.IntegerField()
    price = models.IntegerField()
    used = models.IntegerField()
    disponible = models.IntegerField()
    