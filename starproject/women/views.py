from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404
from .models import *
from .forms import AddPostForm
from django.views.generic import ListView, DetailView, CreateView
# Create your views here.

class WomenHome(ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['cat_selected'] = 0
        return context
    def get_queryset(self) -> QuerySet[Any]:
        return Women.objects.filter(is_published=True)
# def index(request): #HttpRequest
#     posts = Women.objects.all()
#     context = {
#         'posts': posts,
#         'title': 'Главная страница',
#         'cat_selected': 0,
#     }
#     return render(request, 'women/index.html', context=context)

def about(request):
    return render(request, 'women/about.html', {'title': 'О сайте'})

def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Авторизация")

# def addpage(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             #print(form.cleaned_data)
#             form.save()
#             return redirect('home')
#     else:
#         form = AddPostForm()
#     return render(request, 'women/addpage.html', {'form':form, 'title': 'Добавление статьи'})
class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'women/addpage.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление статьи'
        return context

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")

# def show_post(request, post_slug):
#     post = get_object_or_404(Women, slug=post_slug)

#     context = {
#         'post': post,
#         'title': post.title,
#         'cat_selected': post.cat_id,
#     }

#     return render(request, 'women/post.html', context=context)
class ShowPost(DetailView):
    model = Women
    template_name = 'women/post.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'


# def show_category(request, cat_slug):
#     category = get_object_or_404(Category, slug=cat_slug)
#     posts = Women.objects.filter(cat_id=category.pk)
#     #cats = Category.objects.all()
#     if len(posts) == 0:
#         raise Http404()
#     context = {
#         'posts': posts,
#         'title': 'Главная страница',
#         'cat_selected': category.pk,
#     }
#     return render(request, 'women/index.html', context=context)
class WomenCategory(ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self) -> QuerySet[Any]:
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)
    
    def get_context_data(self, *, object_list=None, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категория - ' + str(context['posts'][0].cat)
        context['cat_selected'] = context['posts'][0].cat_id
        return context