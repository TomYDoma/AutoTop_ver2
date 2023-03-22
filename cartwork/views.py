from django.shortcuts import redirect, get_object_or_404, render
from django.views.decorators.http import require_POST
from work.models import Work
from .cartwork import CartWork
from .forms import CartAddWorksForm

@require_POST
def cartwork_add(request, product_id):
    cartwork = CartWork(request)
    product = get_object_or_404(Work, id=product_id)
    form = CartAddWorksForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cartwork.add(product=product, quantity=1)
    return redirect('work:work_list')

def cartwork_remove(request, product_id):
    cartwork = CartWork(request)
    work = get_object_or_404(Work, id=product_id)
    cartwork.remove(work)
    return redirect('cartwork:cartwork_detail')

def cartwork_detail(request):
    cartwork = CartWork(request)
    for item in cartwork:
        pass
    return render(request, 'cartwork/cartWork_detail.html', {'cartwork': cartwork})