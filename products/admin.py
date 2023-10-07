from django.contrib import admin

from products.models import (Basket, ImagesProducts, ProductOptions, Products,
                             ProductsCategories, Testimonials)


class GalleryInline(admin.TabularInline):
    fk_name = 'product'
    model = ImagesProducts


class OptionsInline(admin.TabularInline):
    fk_name = 'product'
    model = ProductOptions


class TestimonialsInline(admin.TabularInline):
    fk_name = 'product'
    model = Testimonials


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    fields = (('name', 'description', 'category'), ('price', 'quantity', 'image'))
    inlines = [GalleryInline, OptionsInline, TestimonialsInline]


admin.site.register(Testimonials)
admin.site.register(ProductsCategories)
admin.site.register(ImagesProducts)
admin.site.register(ProductOptions)
admin.site.register(Basket)
