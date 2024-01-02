from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import *


def index(requests):
    news_categories = NewsType.objects.all()
    news_data_list = News.objects.all()[20:100]
    return render(requests, "index.html", locals())


def login(request):
    return render(request, "login.html")


def category(request, category_id):
    news_categories = NewsType.objects.all()
    news_data_list = News.objects.filter(news_type_id=category_id)
    # return HttpResponse(news_data_list)
    return render(request, "category.html", locals())


def register(request):
    return render(request, "register.html")


def detail(request, new_id):


    new_detail = get_object_or_404(NewsContent, news_id=new_id)
    new_type_id = new_detail.news.news_type_id
    news_data_list = News.objects.filter(news_type_id=new_type_id)
    new_content = new_detail.content
    return render(request, "detail.html", locals())
