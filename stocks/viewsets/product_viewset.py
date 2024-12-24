from rest_framework import viewsets
from stocks.models.produit_model import ProductModel
from stocks.serializers.product_serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
    