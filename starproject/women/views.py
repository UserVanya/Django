from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect
from .models import *
# Create your views here.
menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]
def index(request): #HttpRequest
    posts = Women.objects.all()
    return render(request, 'women/index.html', {'posts':posts, 'menu': menu, 'title': 'Главная страница'})

def about(request):
    return render(request, 'women/about.html', {'title': 'О сайте'})

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")