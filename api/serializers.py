from django.db import models
from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'stock', 'measure', 'price', 'updated_at')


class ProductTotalCostSerializer(serializers.ModelSerializer):
    amount = serializers.IntegerField()

    class Meta:
        model = Product
        fields = ('id', 'title', 'stock', 'measure',
                  'price', 'updated_at', 'amount')
