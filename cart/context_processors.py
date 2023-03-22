from cartwork.cartwork import CartWork
from .cart import Cart

def cart(request):
    return {'cart': Cart(request), 'work': CartWork(request)}