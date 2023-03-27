from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from datetime import date
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
    order = get_object_or_404(Order, pk=pk)
    autopart = order.total_autopart()
    work = order.total_work()
    car = order.ID_Car.get_car()
    carVin = order.ID_Car.get_vin()
    carPTS = order.ID_Car.get_pts()
    carType = order.ID_Car.get_typeCar()
    carColor = order.ID_Car.get_color()
    carNumber = order.ID_Car.get_stateNumber()
    carDate = order.ID_Car.get_Date()
    carMilage = order.ID_Car.get_mileage()
    zagolovok = order.__str__()

    price = str(order.total_price())
    date_now = date.today()


    user = request.user
    f_name = user.first_name
    l_name = user.last_name
    m_name = user.profile.middleName
    addres = user.profile.addres
    number_phone = user.profile.numberPhone



    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="file.pdf"'
    w, h = A4
    p = canvas.Canvas(response)
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

    p.drawString(30, 590, 'Заказанные атвозапчасти:')
    j = 580
    for i in autopart:
        p.drawString(30, j, i)
        j -= 10
    j -= 30

    p.drawString(30, j, 'Работы:')
    for i in work:
        j -= 10
        p.drawString(30, j, i)

    j -= 30

    p.drawString(275, j, 'Дата печати документа: {date_now}'.format(date_now=date_now))
    j -= 10
    p.drawString(275, j, 'Итого к оплате:')
    p.drawString(400, j, "{price}, рублей".format(price=price))
    p.line(378, j-1, 580, j-1)

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
