from django.db import models
from base.models.date_time_model import DateTimeModel

class ProductionModel(DateTimeModel):
    article_id = models.IntegerField()
    intrant_id = models.IntegerField()
    user_applyed = models.CharField( max_length=50)