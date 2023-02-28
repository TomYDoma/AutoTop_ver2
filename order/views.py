from django.shortcuts import render
from django.views.generic import ListView

from order.models import Order


# Create your views here.


class OrderListView(ListView):
    model = Order
    template_name = 'order/orders.html'





























