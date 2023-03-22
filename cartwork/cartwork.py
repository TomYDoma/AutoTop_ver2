from django.conf import settings
from django.forms import model_to_dict

from work.models import Work


class CartWork(object):

    def __init__(self, request):
        """
        Инициализируем корзину
        """
        self.session = request.session
        cart = self.session.get(settings.WORK_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.WORK_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False):
        """
        Добавить продукт в корзину или обновить его количество.
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += 1
        self.save()

    def save(self):
        # Обновление сессии cart
        self.session[settings.WORK_SESSION_ID] = self.cart
        # Отметить сеанс как "измененный", чтобы убедиться, что он сохранен
        self.session.modified = True

    def remove(self, work):

        product_id = str(work.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):

        product_ids = self.cart.keys()
        # получение объектов product и добавление их в корзину
        products = Work.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['name'] = product.name
            self.cart[str(product.id)]['product'] = product.name
            self.cart[str(product.id)]['id'] = product.id

        for item in self.cart.values():
            item['price'] = float(item['price'])
            item['total_price'] = item['price'] * 1
            item['id'] = item['id']
            yield item

    def __len__(self):
        """
        Подсчет всех товаров в корзине.
        """
        return sum(1 for item in self.cart.values())

    def get_total_price(self):
        """
        Подсчет стоимости товаров в корзине.
        """
        return sum(float(item['price']) * 1 for item in
                   self.cart.values())

    def clear(self):
        # удаление корзины из сессии
        del self.session[settings.WORK_SESSION_ID]
        self.session.modified = True