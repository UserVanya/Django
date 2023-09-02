from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect
from .models import *
# Create your views here.

def index(request): #HttpRequest
    posts = Women.objects.all()
    #cats = Category.objects.all()
    context = {
        'posts': posts,
    #    'cats': cats,
    #    'menu': menu,
        'title': 'Главная страница',
        'cat_selected': 0,
    }
    return render(request, 'women/index.html', context=context)

def about(request):
    return render(request, 'women/about.html', {'title': 'О сайте'})

def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Авторизация")

def addpage(request):
    return HttpResponse("Добавление статьи")

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")

def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")

def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)
    #cats = Category.objects.all()
    if len(posts) == 0:
        raise Http404()
    context = {
        'posts': posts,
    #    'cats': cats,
    #    'menu': menu,
        'title': 'Главная страница',
        'cat_selected': cat_id,
    }
    return render(request, 'women/index.html', context=context)