from django.db import models
from base.models.named_model import NamedModel
# Create your models here.

class UserModel(NamedModel):
    prenom = models.CharField(max_length=255)
    birthday = models.DateField()
    email = models.EmailField()
    password = models.CharField(max_length=255)