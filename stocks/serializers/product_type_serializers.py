from rest_framework import serializers
from stocks.models.product_type_model import ProductTypeModel

class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductTypeModel
        fields = '__all__'