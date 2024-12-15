from rest_framework import serializers
from stocks.models.intrant_model import IntrantModel

class IntrantSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntrantModel
        fields = '__all__'