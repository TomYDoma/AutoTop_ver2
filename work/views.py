from django.shortcuts import render, get_object_or_404

from cartwork.forms import CartAddWorksForm
from work.models import CategoryWork, Work


def work_list(request, category_slug=None):
    category = None
    categories = CategoryWork.objects.all()
    products = Work.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(CategoryWork, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'work/list_work.html',
                  {'category': category, 'categories': categories,
                   'products': products})


def work_detail(request, id, slug):
    product = get_object_or_404(Work, id=id, slug=slug, available=True)
    cart_work_form = CartAddWorksForm()
    return render(request, 'work/work_detail.html',
                  {'product': product, 'cart_work_form': cart_work_form})
