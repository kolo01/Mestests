from rest_framework import viewsets
from stocks.models.article_model import ArticleModel
from stocks.serializers.article_serializers import ArticleSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = ArticleModel.objects.all()
    serializer_class = ArticleSerializer