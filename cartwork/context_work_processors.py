from .cartwork import CartWork


def work(request):
    return {'work': CartWork(request)}