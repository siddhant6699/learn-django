from dataclasses import field
from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    # my_discount = serializers.SerializerMethodField(read_only=True)
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'content',
            'price',
            # 'sale_price',
            # 'get_discount',
        ]

        # def get_my_discount(self, obj):
        #     return obj.get_discount()
