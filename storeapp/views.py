from django.shortcuts import render
from django.views.generic import ListView

from .models import Product


class ProductListView(ListView):
    model = Product
    queryset = Product.objects.all()
    template_name = 'index.html'
    extra_context = {
        'categories': [1, 2]
    }
