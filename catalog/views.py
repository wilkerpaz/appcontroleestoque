from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Product, Category


class ProductListView(generic.ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'
    paginate_by = 2


class CategoryListVew(generic.ListView):
    template_name = 'catalog/category.html'
    context_object_name = 'product_list'
    paginate_by = 2

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(CategoryListVew, self).get_context_data(**kwargs)
        context['current_category'] = get_object_or_404(Category, slug=self.kwargs['slug'])
        return context


def product(request, slug):
    context = {
        'product': Product.objects.get(slug=slug)
    }
    return render(request, 'catalog/product.html', context)


product_list = ProductListView.as_view()
category = CategoryListVew.as_view()

# hugo moutine

# def category(request, slug):
#     category_filter = Category.objects.get(slug=slug)
#     context = {
#         'current_category': category_filter,
#         'product_list': Product.objects.filter(category=category_filter),
#     }
#     return render(request, 'catalog/category.html', context)
