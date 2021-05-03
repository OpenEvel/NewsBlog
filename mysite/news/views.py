from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
# Create your views here.
from .forms import NewsForm
from .models import *


def index(request):
    news = News.objects.all()
    context = {
        "news": news,
        "title": "Список новостей"
    }
    return render(request, 'news/index.html', context=context)

def test(request):
    print(request)
    return HttpResponse('<h1>Тестовая страница<h1>')


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    context = {
        "news": news,
        "title": category.title
    }
    return render(request, template_name='news/category.html', context=context)

def view_news(request, news_id):
    news_item = get_object_or_404(News, pk=news_id)
    return render(request, template_name='news/view_news.html', context={"news_item": news_item})

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


