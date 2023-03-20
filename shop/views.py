from django.shortcuts import render, get_object_or_404

from cart.forms import CartAddProductForm
from shop.models import Category, Autopart


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Autopart.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/list_autopart.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Autopart,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/autopart_detail.html', {'product': product,
                                                        'cart_product_form': cart_product_form})