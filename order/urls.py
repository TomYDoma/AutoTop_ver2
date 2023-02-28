from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from .views import OrderListView

urlpatterns = [
    #path('feedback_new', views.createFeedback, name='feedback_new'),

    path('', OrderListView.as_view(), name="order"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
