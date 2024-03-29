# Generated by Django 4.1.3 on 2023-02-17 17:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0033_delete_work'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0014_remove_order_car_remove_order_client_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autopart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='autopart/%Y/%m/%d')),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.PositiveIntegerField()),
                ('available', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Автозапчасть',
                'verbose_name_plural': 'Автозапчасти',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='CompositionOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_Autopart', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='order.autopart')),
                ('ID_Employee', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.specialistlist')),
            ],
            options={
                'verbose_name': 'Состав заказов по работам',
                'verbose_name_plural': 'Составы заказов по работам',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Статус',
                'verbose_name_plural': 'Статусы',
            },
        ),
        migrations.CreateModel(
            name='TypesWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50, verbose_name='Название работы')),
                ('Price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Стоимость')),
                ('Execution_Time', models.IntegerField(verbose_name='Срок выполнения')),
                ('Warranty', models.IntegerField(verbose_name='Гарантия')),
            ],
            options={
                'verbose_name': 'Вид работы',
                'verbose_name_plural': 'Виды работ',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Start_Date', models.DateTimeField(auto_now_add=True)),
                ('End_Date', models.DateTimeField(auto_now=True)),
                ('Cost', models.IntegerField(verbose_name='Стоимость')),
                ('ID_Car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.car')),
                ('ID_Client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('ID_CompositionOrder', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='order.compositionorder')),
                ('Status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='order.status')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.AddField(
            model_name='compositionorder',
            name='ID_TypesWorks',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='order.typeswork'),
        ),
        migrations.AddField(
            model_name='autopart',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='autopart', to='order.category'),
        ),
        migrations.AlterIndexTogether(
            name='autopart',
            index_together={('id', 'slug')},
        ),
    ]
