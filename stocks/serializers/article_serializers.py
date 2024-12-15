from rest_framework import serializers
from stocks.models.article_model import ArticleModel

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleModel
        fields = '__all__'