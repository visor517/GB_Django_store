from django.shortcuts import render
from django.views.generic import ListView

from .models import Category, Product


class ProductListView(ListView):
    model = Product
    template_name = 'index.html'
    extra_context = {
        'categories': Category.objects.all()
    }

    def get_queryset(self):
        if 'pk' in self.kwargs:
            return Product.objects.prefetch_related('categories').filter(categories=self.kwargs['pk'])
        return Product.objects.prefetch_related('categories').all()