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