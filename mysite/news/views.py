from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
# Create your views here.
from .forms import NewsForm
from .models import *

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from django.contrib.auth.mixins import LoginRequiredMixin

from .utils import MyMixin


class HomeNews(MyMixin, ListView):
    model = News
    template_name = 'news/home_news_list.html'  # переопределям название шаблона
    context_object_name = 'news'  # обект с которым хотим работать
    mixin_prop = 'hello_world'

    # extra_context = {'title': 'Список новостей'} # дополнительные данные - ТОЛЬКО СО СТАТИЧНЫМИ ДАННЫМИ

    def get_context_data(self, *, object_list=None, **kwargs):  # позволяет добавлять в контекст динамические данные
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_upper('Главная страница')
        context['mixin_prop'] = self.get_prop()
        return context

    def get_queryset(self):  # позволяет фильтровать queryset из модели/ нужный нам набор объектов
        return News.objects.filter(is_published=True)


"""
def index(request):
    news = News.objects.all()
    context = {
        "news": news,
        "title": "Список новостей"
    }
    return render(request, 'news/index.html', context=context)
"""


class NewsByCategory(MyMixin, ListView):
    model = News
    template_name = 'news/home_news_list.html'  # переопределям название шаблона
    context_object_name = 'news'  # обект с которым хотим работать

    # extra_context = {'title': 'Список новостей'} # дополнительные данные - ТОЛЬКО СО СТАТИЧНЫМИ ДАННЫМИ

    def get_context_data(self, *, object_list=None, **kwargs):  # позволяет добавлять в контекст динамические данные
        context = super().get_context_data(**kwargs)
        # category = News.objects.filter(category_id=self.kwargs['category_id'])
        # context['title'] = category.title
        context['title'] = self.get_upper(Category.objects.get(pk=self.kwargs['category_id']))
        return context

    def get_queryset(self):  # позволяет фильтровать queryset из модели/ нужный нам набор объектов
        return News.objects.filter(category_id=self.kwargs['category_id'])


'''def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    context = {
        "news": news,
        "title": category.title
    }
    return render(request, template_name='news/category.html', context=context)'''


def test(request):
    print(request)
    return HttpResponse('<h1>Тестовая страница<h1>')


class ViewNews(DetailView):
    model = News
    # pk_url_kwarg = 'news_id'
    # template_name = 'news/news_detail.html'
    context_object_name = 'news_item'


'''
def view_news(request, news_id):
    news_item = get_object_or_404(News, pk=news_id)
    return render(request, template_name='news/view_news.html', context={"news_item": news_item})'''


class CreateNews(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    # success_url = reverse('home')
    # login_url = '/admin/'
    raise_exception = True # Вызывает ошибку 403

def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data) # если поля формы проходят валидацию они попадают в словарь cleaned_data
            # News.objects.create(**form.cleaned_data) # ** - распаковка словарей
            # return redirect('home')
            # news = News.objects.create(**form.cleaned_data) # ** - распаковка словарей
            news = form.save() # в случае с forms.ModelForm
            return redirect(news)

    else:
        form = NewsForm()
    return render(request, 'news/add_news.html', {"form": form})

