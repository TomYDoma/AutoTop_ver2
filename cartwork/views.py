from django.shortcuts import redirect, get_object_or_404, render
from django.views.decorators.http import require_POST

from work.models import Work
from .cartwork import CartWork
from .forms import CartAddWorksForm


# Create your views here.
@require_POST
def cartwork_add(request, product_id):
    cartwork = CartWork(request)
    product = get_object_or_404(Work, id=product_id)
    form = CartAddWorksForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cartwork.add(product=product, quantity=1,
                 update_quantity=cd['update'])
    return redirect('cartwork:cartwork_detail')

def cartwork_remove(request, product_id):
    cartwork = CartWork(request)
    product = get_object_or_404(Work, id=product_id)
    cartwork.remove(product)
    return redirect('cartwork:cartwork_detail')

def cartwork_detail(request):
    cartwork = CartWork(request)
    for item in cartwork:
        item['update_quantity_form'] = CartAddWorksForm(
            initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'cartwork/cartWork_detail.html', {'cartwork': cartwork})