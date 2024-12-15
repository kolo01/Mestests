from rest_framework import viewsets
from stocks.models.providers_model import ProviderModel
from stocks.serializers.providers_serializers import ProviderSerializer

class ProviderViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = ProviderModel.objects.all()
    serializer_class = ProviderSerializer