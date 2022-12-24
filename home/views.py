from PIL import Image
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from .forms import FeedbackListForm
from django.http import HttpResponse


from .models import SpecialistAdmin, SpecialistList, mainCart, FeedbackList


class mainCart(ListView):
    model = mainCart
    template_name = 'home/index.html'


def contact(request):
    return render(request, 'home/contact.html')


def services(request):
    return render(request, 'home/services.html')

def useful(request):
    return render(request, 'home/useful.html')


class SmecListView(ListView):
    model = SpecialistList
    template_name = 'home/team_specialist.html'

class SmecAdminListView(ListView):
    model = SpecialistAdmin
    template_name = 'home/team_admin.html'






def createFeedback(request):
    eror = ''
    if request. method == 'POST':
        form = FeedbackListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            eror = 'Форма была неверной'

    form = FeedbackListForm()
    data = {
        'form': form,
        'eror': eror
    }
    return render(request, 'home/feedback.html', data)
