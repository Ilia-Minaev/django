from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    # print(request)
    return HttpResponse('Hello')


def test(request):
    # print(request)
    return HttpResponse('<h1>test</h1>')
