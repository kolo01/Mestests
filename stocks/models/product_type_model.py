
from django.db import models
from base.models.labelled_model import LabelledModel

class ProductTypeModel(LabelledModel):
    category = models.CharField(max_length=255)
    