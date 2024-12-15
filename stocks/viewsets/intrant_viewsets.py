from rest_framework import viewsets
from stocks.models.intrant_model import IntrantModel
from stocks.serializers.intrant_serializers import IntrantSerializer

class IntrantViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = IntrantModel.objects.all()
    serializer_class = IntrantSerializer