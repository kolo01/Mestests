from rest_framework import viewsets
from stocks.models.product_type_model import ProductTypeModel
from stocks.serializers.product_type_serializers import ProductTypeSerializer

class ProductTypeViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = ProductTypeModel.objects.all()
    serializer_class = ProductTypeSerializer