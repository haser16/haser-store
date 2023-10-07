from rest_framework import serializers

from products.models import Products


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Products
        fields = ('name', 'description', 'price', 'quantity', 'category', 'image')
