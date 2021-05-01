from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import *


def index(request):
    news = News.objects.all()

    return render(request, 'news/index.html', {'news': news, 'title': 'Список новостей'})

def test(request):
    print(request)
    return HttpResponse('<h1>Тестовая страница<h1>')