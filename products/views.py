from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.views import View



class ProductView(View):
    def get(self, request):
        return render(request, "products.html", {'produits': 'HP'})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product_detail.html', {'product': product})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def category_detail(request, pk):
    category = get_object_or_404(Category, id=pk)
    products = category.products.all()  # Utilisation de related_name='products'
    return render(request, 'category_detail.html', {'category': category, 'products': products})