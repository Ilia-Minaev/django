from django.shortcuts import render, get_object_or_404
from .models import News, Category
from .forms import NewsForm
# Create your views here.


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
        form = NewsForm()
    else:
        form = NewsForm()
    context = {
        'title': 'Добавление новости',
        'h1': 'Добавление новости',
        'form': form,
    }
    return render(request, template_name='news/add_news.html', context=context)
