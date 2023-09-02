from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect
from .models import *
# Create your views here.
menu = [{"title":"О сайте", "url_name":"about"},
        {"title":"Добавить статью", "url_name":"add_page"},
        {"title":"Обратная связь", "url_name":"contact"},
        {"title":"Войти", "url_name":"login"}]
 
def index(request): #HttpRequest
    posts = Women.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница'
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