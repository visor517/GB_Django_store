from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render
from django.views.generic import ListView

from .models import Category, Product


class ProductListView(ListView):
    model = Product
    template_name = '../templates/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update({
            'categories': Category.on_site.all(),
            'site': get_current_site(request=self.request),
        })
        return context

    def get_queryset(self):
        if 'pk' in self.kwargs:
            return Product.on_site.prefetch_related('categories').filter(categories=self.kwargs['pk'])
        return Product.on_site.prefetch_related('categories').all()
