from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from .models import News, Category
from .forms import NewsForm


class HomeNews(ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    # extra_context = {'title': 'Главная', }

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self) -> QuerySet[Any]:
        # return News.objects.filter(id_published=True)
        return super().get_queryset().filter(id_published=True)


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


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)

    category = Category.objects.get(pk=category_id)
    context = {
        'title': 'Список новостей',
        'news': news,
        'category': category,
    }
    return render(request, template_name='news/category.html', context=context)


def view_news(request, news_id):
    # news_item = News.objects.get(pk=news_id)
    news_item = get_object_or_404(News, pk=news_id)
    context = {
        'title': news_item.title,
        'news_item': news_item,
    }
    return render(request, template_name='news/view_news.html', context=context)


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
