from django.urls import path
from . import views

urlpatterns = [
    path("", views.product_list, name="product_list"),
    path("<int:id>/", views.product_detail, name="product_detail"),
    path("cart/", views.cart, name="cart"),
    path("add-to-cart/<int:id>/", views.add_to_cart, name="add_to_cart"),
]