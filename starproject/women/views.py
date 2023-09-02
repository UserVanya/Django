from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect, get_object_or_404
from .models import *
from .forms import AddPostForm
# Create your views here.

def index(request): #HttpRequest
    posts = Women.objects.all()
    context = {
        'posts': posts,
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
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            #print(form.cleaned_data)
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()
    return render(request, 'women/addpage.html', {'form':form, 'title': 'Добавление статьи'})

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")

def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)

    context = {
        'post': post,
        'title': post.title,
        'cat_selected': post.cat_id,
    }

    return render(request, 'women/post.html', context=context)

def show_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    posts = Women.objects.filter(cat_id=category.pk)
    #cats = Category.objects.all()
    if len(posts) == 0:
        raise Http404()
    context = {
        'posts': posts,
        'title': 'Главная страница',
        'cat_selected': category.pk,
    }
    return render(request, 'women/index.html', context=context)