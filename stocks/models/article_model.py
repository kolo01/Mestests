from django.db import models
from base.models.labelled_model import LabelledModel

class ArticleModel(LabelledModel):
    quantity = models.IntegerField()
    price = models.IntegerField()
    selled = models.IntegerField()
    disponible = models.IntegerField()
    
    