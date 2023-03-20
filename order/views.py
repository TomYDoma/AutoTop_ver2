from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView

from cart.cart import Cart
from order.forms import OrderCreateForm
from order.models import Order, OrderItem, Status


class OrderListView(ListView):
    model = Order
    template_name = 'order/orders.html'

class OrderDetailView(DetailView): # новое
    model = Order
    template_name = 'order/order_detail.html'


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.status = get_object_or_404(Status, pk=1)
            instance.ID_Client = request.user
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'],
                                         quantity=item['quantity'])
                # clear the cart
            cart.clear()
            return render(request, 'order/order_new.html',
                          {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'order/order_new.html',
                  {'cart': cart, 'form': form})























