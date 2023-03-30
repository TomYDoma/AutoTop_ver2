from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static

from order import views
from .views import OrderListView, OrderDetailView, OrderPayView

app_name = 'order'
urlpatterns = [
    #path('feedback_new', views.createFeedback, name='feedback_new'),
    path('', OrderListView.as_view(), name="order"),
    path('new/', views.order_create, name='order_new'),
    path('<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
    path('pay/<int:pk>/', OrderPayView.as_view(), name='order_pay'),
    path('<int:pk>/processingPay/', views.payment_order, name='payment_order'),

    path('<int:pk>/pdf', views.getpdf, name='pdf')




] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
