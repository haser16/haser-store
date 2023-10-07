from rest_framework.generics import ListAPIView

from products.models import Products
from products.serializers import ProductSerializer


class ProductListApiView(ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
