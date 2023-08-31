from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect
# Create your views here.

def index(request): #HttpRequest
    return HttpResponse("Страница women")

def categories(request, cat):
    if(request.GET):
        print(request.GET)
    return HttpResponse(f"<h1>Статьи по категориям </h1> {cat}")

def archive(request, year):
    if int(year) > 2023:
        #raise Http404()
        return redirect('home', permanent=True)

    return HttpResponse(f"<h1>Архив по годам</h1> <p>{year}</p>")

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")