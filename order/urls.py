from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static

from . import views
from .views import OrderListView, OrderDetailView


app_name = 'order'
urlpatterns = [
    #path('feedback_new', views.createFeedback, name='feedback_new'),
    path('', OrderListView.as_view(), name="order"),
    path('<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
    path('new/', views.order_create, name='order_new'),
    path('<int:pk>/pdf', views.getpdf, name='pdf')




] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
