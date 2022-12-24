from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from .forms import LoginForm
from .views import SignUpView, CustomLoginView, ResetPasswordView, profile, ChangePasswordView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='registration/login.html',
                                           authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    #path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
    #path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html', name='password_reset_confirm'),
    #path('password-reset-complete/',
        #    auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
        #    name='password_reset_complete'),
        #    name='password_reset_confirm'),
    path('profile/', profile, name='users-profile'),
    path('password-change/', ChangePasswordView.as_view(), name='password_change'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)