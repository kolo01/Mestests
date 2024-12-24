from django.db import models
from base.models.labelled_model import LabelledModel
from .providers_model import ProviderModel
from  .product_type_model import ProductTypeModel

class ProductModel(LabelledModel):
    fournisseur = models.ForeignKey(ProviderModel, on_delete=models.CASCADE)
    productType = models.ForeignKey(ProductTypeModel, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()
    selled = models.IntegerField()
    disponible = models.IntegerField()