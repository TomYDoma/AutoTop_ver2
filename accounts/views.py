from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.views import View
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from .forms import RegisterForm, LoginForm, CarForm, CarEditForm
from .forms import UpdateUserForm, UpdateProfileForm
from .models import Car


class CustomLoginView(LoginView):
    form_class = LoginForm


class SignUpView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'registration/signup.html'

    def dispatch(self, request, *args, **kwargs):
        # will redirect to the home page if a user tries to access the register page while logged in
        if request.user.is_authenticated:
            return redirect(to='/')

        # else process dispatch as it otherwise normally would
        return super(SignUpView, self).dispatch(request, *args, **kwargs)
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Аккаунт создан:  {username}')

            return redirect(to='/')

        return render(request, self.template_name, {'form': form})


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'registration/password_reset.html'
    email_template_name = 'registration/password_reset_email.html'
    subject_template_name = 'registration/password_reset_subject.txt'
    success_message = "Мы отправили вам по электронной почте инструкции по установке вашего пароля," \
                      "если существует учетная запись с указанным вами адресом электронной почты. Вы должны получить их в ближайшее время." \
                      " Если вы не получили электронное письмо, " \
                      "пожалуйста, убедитесь, что вы ввели адрес, по которому регистрировались, и проверьте папку со спамом."
    success_url = reverse_lazy('home')

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Ваш профиль успешно изменен')
            return redirect(to='users-profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'registration/profile.html', {'user_form': user_form, 'profile_form': profile_form})

class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'registration/change_password.html'
    success_message = "Пароль пользователя успешно изменен"
    success_url = reverse_lazy('home')



class CarListView(ListView):
    model = Car
    template_name = 'registration/car.html'


class CarDetailView(DetailView):
    model = Car
    template_name = 'registration/car_detail.html'


class CarCreateView(CreateView):
    model = Car
    template_name = 'registration/car_new.html'
    form_class = CarForm

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.author = self.request.user
        instance.Relese_Date = datetime.now()
        form.save()
        return super(CarCreateView, self).form_valid(form)


class CarUpdateView(UpdateView):  # Новый класс
    model = Car
    template_name = 'registration/car_edit.html'
    form_class = CarEditForm


class CarDeleteView(DeleteView): # Создание нового класса
    model = Car
    template_name = 'registration/car_delete.html'
    success_url = reverse_lazy('car')