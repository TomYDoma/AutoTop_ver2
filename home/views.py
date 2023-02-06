from PIL import Image
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView
from .forms import FeedbackListForm, CommentForm
from .models import SpecialistAdmin, SpecialistList, mainCart, FeedbackList, Articles, Comment, Work


def mainCartt(request):
    news = mainCart.objects.order_by('-date')[:4]
    return render(request, 'home/index.html', {'news': news})

def contact(request):
    return render(request, 'home/contact.html')

class ServicesListView(ListView):
    model = Work
    template_name = 'home/services.html'


class NewsDetailView(DetailView):
    model = Articles
    form_class = CommentForm()
    template_name = 'home/detail_news.html'
    context_object_name = 'article'
    def get_context_data(self, *args, **kwargs):
        comm = super(NewsDetailView, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        comm['comments'] = Comment.objects.filter(article=pk)
        return comm

def createComment(request, id):
    news = Articles.objects.filter(id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        article = Articles.objects.get(pk=id)
        print(article)
        if form.is_valid():
            comm = form.save(False)
            comm.author_id = request.user.id
            #Эта дура не хочет получать id записи, к которой
            # нужно оставить комент, поэтому тут заглушка
            comm.article_id = article.id
            form.save()
            return redirect('news-detail', id)
        else:
            eror = 'Форма была неверной'
    form = CommentForm()
    data = {
        'form': form,
    }
    return render(request, 'home/new_comment.html', data)

#Сейчас пользователь может удалять любой комментарий, нужно поставить запрет на
# удаление чужих комментов

class BlogDeleteView(DeleteView):
    model = Comment
    template_name = 'home/post_delete.html'
    success_url = reverse_lazy('useful')


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
