from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# Create your views here.
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