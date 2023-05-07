from django.shortcuts import render
from django.http import HttpResponse
from .models import News
# Create your views here.


def index(request):
    news = News.objects.order_by('-created_at')
    # res = '<h1>Список новостей</h1>'
    # for item in news:
    #    res += f'<div><p>{item.title}</p></div>'
    #    res += f'<div><p>{item.content}</p></div>'
    #    res += f'<hr>'
    # return HttpResponse(res)
    return render(request, 'news/index.html', {'news': news, 'title': 'Список новостей'})
