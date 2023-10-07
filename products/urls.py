from django.urls import path

from products.views import IndexTemplateView, ProductTemplateView

app_name = 'products'

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('product/<str:category>/', IndexTemplateView.as_view(), name='category'),
    path('page/<int:page>/', IndexTemplateView.as_view(), name='paginator'),
    path('page/<str:product>/', IndexTemplateView.as_view(), name='paginator'),
    path('products/<int:product_id>/', ProductTemplateView.as_view(), name='product'),
]
