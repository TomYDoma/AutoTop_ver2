from os.path import join

from PIL import Image
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

from cart.cart import Cart
from cartwork.cartwork import CartWork
from order.forms import OrderCreateForm
from order.models import Order, OrderItem, Status, OrderWork


class OrderListView(ListView):
    model = Order
    template_name = 'order/orders.html'


class OrderDetailView(DetailView):  # новое
    model = Order
    template_name = 'order/order_detail.html'


def getpdf(request, pk):

    print(type(pk))
    order = get_object_or_404(Order, pk=pk)
    text = order.total_autopart()
    car = order.ID_Car.get_car()
    carVin = order.ID_Car.get_vin()
    carPTS = order.ID_Car.get_pts()
    carType = order.ID_Car.get_typeCar()
    carColor = order.ID_Car.get_color()
    carNumber = order.ID_Car.get_stateNumber()
    carDate = order.ID_Car.get_Date()
    carMilage = order.ID_Car.get_mileage()
    zagolovok = order.__str__()

    user = request.user
    f_name = user.first_name
    l_name = user.last_name
    m_name = user.profile.middleName
    addres = user.profile.addres
    number_phone = user.profile.numberPhone
    print(m_name)


    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="file.pdf"'
    w, h = A4
    p = canvas.Canvas(response, pagesize=A4)
    pdfmetrics.registerFont(TTFont('FreeSans', 'order/FreeSans.ttf'))
    p.setFont("FreeSans", 15)

    p.drawString(100, 800, zagolovok)

    img = ImageReader("static/img/logo_small.png")

    p.drawImage(img, 450, 750)

    p.setFont("FreeSans", 10)

    p.drawString(450, 740, 'ООО «AutoTop»')
    p.drawString(450, 730, 'ИНН: 6150004220')
    p.drawString(450, 720, 'КПП: 615001001')
    p.drawString(450, 710, 'ОГРН: 1026102222772')

    p.drawString(30, 740, 'Заказчик:  {l_name} {f_name} {m_name}'.format(f_name=f_name, l_name=l_name, m_name=m_name))
    p.drawString(30, 725, 'Телефон: {number_phone}'.format(number_phone=number_phone))
    p.drawString(30, 710, 'Адрес: {addres}'.format(addres=addres))
    p.drawString(30, 695, 'ПТС: {carPTS}'.format(carPTS=carPTS))


    p.drawString(30, 650, 'Марка и модель ТС: {car}'.format(car=car))
    p.drawString(30, 640, 'VIN: {carVin}'.format(carVin=carVin))
    p.drawString(30, 630, 'Гос. Номер: {carNumber}'.format(carNumber=carNumber))
    p.drawString(30, 620, 'Пробег: {carMilage}'.format(carMilage=carMilage))


    p.drawString(300, 650, 'Тип кузова: {carType}'.format(carType=carType))
    p.drawString(300, 640, 'Цвет: {carColor}'.format(carColor=carColor))
    p.drawString(300, 630, 'Год выпуска: {carDate}'.format(carDate=carDate))


    j = 10
    for i in text:
        p.drawString(20, 600 - j, i)
        j += 10



    p.drawString(275, 100, 'Итого к оплате:')
    p.drawString(500, 100, "$1,000.00")
    p.line(378, 99, 580, 99)


    #p.drawString(100, 700, text)
    p.showPage()
    p.save()
    return response


def order_create(request):
    cart = Cart(request)
    cartwork = CartWork(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.status = get_object_or_404(Status, pk=1)
            instance.ID_Client = request.user
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product_id=item['id'],
                                         quantity=item['quantity'])

            cart.clear()
            for item in cartwork:
                OrderWork.objects.create(order=order, work_id=item['id'])

            cartwork.clear()
            return render(request, 'order/order_new.html',
                          {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'order/order_new.html',
                  {'cart': cart, 'work': cartwork, 'form': form})
