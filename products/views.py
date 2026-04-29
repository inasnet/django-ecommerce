from django.shortcuts import render, get_object_or_404 , redirect
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
def add_to_cart(request, id):
    product = get_object_or_404(Product, id=id)

    cart = request.session.get("cart", {})

    product_id = str(product.id)

    if product_id in cart:
        cart[product_id]["quantity"] += 1
    else:
        cart[product_id] = {
            "name": product.name,
            "price": float(product.price),
            "quantity": 1,
        }

    request.session["cart"] = cart

    return redirect("cart")


def cart(request):
    cart = request.session.get("cart", {})

    total = 0
    for item in cart.values():
        item["total"] = item["price"] * item["quantity"]
        total += item["total"]

    return render(request, "cart.html", {
        "cart": cart,
        "total": total
    })