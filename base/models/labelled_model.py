from django.db import models
from .date_time_model import DateTimeModel


class LabelledModel(DateTimeModel):
    name = models.CharField(max_length=255,null=True)
    
    class meta:
        abstract = True

