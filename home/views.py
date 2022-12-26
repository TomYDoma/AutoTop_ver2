from PIL import Image
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView
from .forms import FeedbackListForm, CommentForm
from django.http import HttpResponse, response

from .models import SpecialistAdmin, SpecialistList, mainCart, FeedbackList, Articles, Comment


def mainCartt(request):
    news = mainCart.objects.order_by('-date')[:4]
    return render(request, 'home/index.html', {'news': news})


def contact(request):
    return render(request, 'home/contact.html')


def services(request):
    return render(request, 'home/services.html')

def createComment(request, pk, *args, **kwargs):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        current_user = request.user.id
        article = Articles.objects.get(pk=pk)
        print(article.id)
        if form.is_valid():
            comm = form.save(False)
            comm.author_id = request.user.id
            #Эта дура не хочет получать id записи, к которой
            # нужно оставить комент, поэтому тут заглушка
            comm.article_id = 1
            form.save()
            return redirect('useful')
        else:
            eror = 'Форма была неверной'
    form = CommentForm()
    data = {
        'form': form
    }
    return render(request, 'home/detail_news.html', data)

class NewsDetailView(DetailView):
    model = Articles
    form_class = CommentForm
    template_name = 'home/detail_news.html'
    context_object_name = 'article'
    def get_context_data(self, *args, **kwargs):
        comm = super(NewsDetailView, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        comm['comments'] = Comment.objects.filter(article=pk)
        return comm



def useful(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'home/useful.html', {'news': news})

def news_filter(request, pk):
    news = Articles.objects.order_by('-date')
    if pk == 1:
        news = Articles.objects.order_by('-date')
    elif pk ==2:
        news = Articles.objects.filter(anons="Детали и обслуживание")
    elif pk == 3:
        news = Articles.objects.filter(anons="Выбор и покупка")
    elif pk == 4:
        news = Articles.objects.filter(anons="Разбор и топы")
    return render(request, 'home/useful.html', {'news': news})



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
