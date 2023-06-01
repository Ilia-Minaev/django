
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout
from django.contrib import messages
# from django.urls import reverse_lazy
# from django.contrib.auth.forms import UserCreationForm

from typing import Any, Dict
from .models import News, Category
from .forms import NewsForm, UserRegisterForm, UserLoginForm
from .utils import MyMixin


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(
                request=request,
                message='Вы успешно зарегистрировались')
            return redirect('home')
        else:
            messages.error(
                request=request,
                message='Ошибка регистрации')
    else:
        form = UserRegisterForm()

    context = {
        'title': 'Регистрация',
        'h1': 'Регистрация',
        'form': form,
    }
    return render(request=request, template_name='news/register.html', context=context)


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    context = {
        'title': 'Вход',
        'h1': 'Вход',
        'form': form,
    }
    return render(request=request, template_name='news/login.html', context=context)


def user_logout(request):
    logout(request)
    return redirect('login')


def test(request):
    objects = ['john', 'mark', 'kate', 'robert',
               'paul', 'ringo', 'django freeman', 'iezecul', '1111 ']
    from django.core.paginator import Paginator
    paginator = Paginator(objects, 2)
    page_num = request.GET.get('page', 1)
    page_objects = paginator.get_page(page_num)
    context = {
        'title': 'Тестовая страница',
        'page_obj': page_objects
    }
    return render(request, 'news/test.html', context)


class HomeNews(MyMixin, ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    # extra_context = {'title': 'Главная', }
    allow_empty = True
    mixin_prop = 'hello world'
    paginate_by = MyMixin.pagination_num

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['mixin_prop'] = self.get_prop()
        return context

    def get_queryset(self) -> QuerySet[Any]:
        # return News.objects.filter(is_published=True)
        return super().get_queryset().filter(is_published=True).select_related('category')


"""
def index(request):
    news = News.objects.order_by('-created_at')

    # res = '<h1>Список новостей</h1>'
    # for item in news:
    #    res += f'<div><p>{item.title}</p></div>'
    #    res += f'<div><p>{item.content}</p></div>'
    #    res += f'<hr>'
    # return HttpResponse(res)
    context = {
        'title': 'Список новостей',
        'news': news,

    }
    return render(request, template_name='news/index.html', context=context)
"""


class NewsByCategory(MyMixin, ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    allow_empty = False
    paginate_by = MyMixin.pagination_num

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        title = Category.objects.get(pk=self.kwargs['category_id'])
        title = self.get_upper(title)
        context = super().get_context_data(**kwargs)
        context['title'] = title
        return context

    def get_queryset(self) -> QuerySet[Any]:
        # return News.objects.filter(is_published=True)
        return super().get_queryset().filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category')


"""
def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)

    category = Category.objects.get(pk=category_id)
    context = {
        'title': 'Список новостей',
        'news': news,
        'category': category,
    }
    return render(request, template_name='news/category.html', context=context)
"""


class ViewNews(DetailView):
    model = News
    # pk_url_kwarg = 'news_id'
    template_name = 'news/news_detail.html'
    context_object_name = 'news_item'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = News.objects.get(pk=self.kwargs['pk'])
        return context

    def get_queryset(self) -> QuerySet[Any]:
        # return News.objects.filter(is_published=True)
        return super().get_queryset().filter(is_published=True)


"""
def view_news(request, news_id):
    # news_item = News.objects.get(pk=news_id)
    news_item = get_object_or_404(News, pk=news_id)
    context = {
        'title': news_item.title,
        'news_item': news_item,
    }
    return render(request, template_name='news/view_news.html', context=context)
"""


class CreateNews(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    # success_url = reverse_lazy('home')
    login_url = '/admin/'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить новость'
        return context


"""
def add_news(request):
    form = ''
    if (request.method == 'POST'):
        form = NewsForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            # news = News.objects.create(**form.cleaned_data)
            news = form.save()
            return redirect(news)
    else:
        form = NewsForm()
    context = {
        'title': 'Добавление новости',
        'h1': 'Добавление новости',
        'form': form,
    }
    return render(request, template_name='news/add_news.html', context=context)
"""
