from PIL import Image
from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse

from .models import SpecialistAdmin


def index(request):
    return render(request, 'home/index.html')


def contact(request):
    return render(request, 'home/contact.html')


def services(request):
    return render(request, 'home/services.html')


def team_specialist(request):
    return render(request, 'home/team_specialist.html')


class SmecAdminListView(ListView):
    model = SpecialistAdmin
    template_name = 'home/team_admin.html'






