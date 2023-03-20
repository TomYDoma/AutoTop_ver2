####Состав заказа
class CompositionOrder(models.Model):
    #ID_Order = models.ForeignKey(Order, on_delete=models.CASCADE)
    ID_TypesWorks = models.ManyToManyField(TypesWork)
    ID_Employee = models.ForeignKey(home.models.SpecialistList, on_delete=models.PROTECT)
    ID_Autopart = models.ManyToManyField(Autopart)

    def __str__(self):
        m = self.ID_TypesWorks.all().values_list('Name', flat=True).annotate()
        print(m)
        n = []
        for i in enumerate(m):
            n += i
            print(i)
        return str(n)

    #str(self.ID_TypesWorks.all().values_list('Name', flat=True).annotate())
    class Meta:
        verbose_name = 'Состав заказов'
        verbose_name_plural = 'Составы заказов'



OrderAutopart.objects.filter(order=self)

a = OrderAutopart.objects.values_list('autopart', flat=True)




class OrderAutopart(models.Model):
    autopart = models.ForeignKey(Autopart, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    count = models.IntegerField(default=1)
    def total(self):
        return self.count * self.autopart.price

    def return_autopart(self):
        return f"{self.autopart}, Количество: {self.count} ШТ"
    def __str__(self):
        return f"{self.autopart.name}, " \
               f"р{self.autopart.price} * {self.count} = Р{self.total()}"
    def get_absolute_url(self):  # Тут мы создали новый метод
        return reverse('order_detail', args=[str(self.order.id)])



#Модель
    def total_price(self):
        i = 0
        for cart_item in self.work.all():
            i += cart_item.return_price()
        j = 0
        for cart_item in self.autopart.all():
            j += cart_item.return_price()
        return sum([j, i])

    def total_work(self):
        return ([
            cart_item.return_work()
            for cart_item in self.work.all()
        ])

    def total_autopart(self):
        return ([
            cart_item.return_autopart()
            for cart_item in self.autopart.all()
        ])



class OrderCreateView(CreateView): # новое изменение
    model = Order
    template_name = 'order/order_new.html'
    fields = ['ID_Car', 'work',]
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.ID_Client = self.request.user
        form.save()
        return super(OrderCreateView, self).form_valid(form)
