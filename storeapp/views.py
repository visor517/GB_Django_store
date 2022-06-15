from django.shortcuts import render
from django.views.generic import ListView

from .models import Category, Product


class ProductListView(ListView):
    model = Product
    queryset = Product.objects.prefetch_related('categories').all()
    template_name = 'index.html'
    extra_context = {
        'categories': Category.objects.all()
    }
