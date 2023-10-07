from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from common.views import TitleMixin
from products.models import Products, ProductsCategories


# Main Page
class IndexTemplateView(TitleMixin, ListView):
    model = Products
    template_name = 'products/index.html'
    paginate_by = 6
    title = 'Haser-Store'

    def get_queryset(self):
        queryset = super(IndexTemplateView, self).get_queryset()
        category = self.kwargs.get('category')

        return queryset.filter(category__name=category) if category else queryset

    def get_context_data(self, **kwargs):
        context = super(IndexTemplateView, self).get_context_data()

        context['categories'] = ProductsCategories.objects.all()

        return context


# Product page
class ProductTemplateView(TitleMixin, TemplateView):
    model = Products
    template_name = 'products/product.html'
    title = 'Product'

    def get_context_data(self, **kwargs):
        context = super(ProductTemplateView, self).get_context_data()

        product_id = self.kwargs.get('product_id')
        context['product'] = Products.objects.filter(id=product_id).first

        return context
