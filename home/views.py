from django.shortcuts import render, get_object_or_404
from .models import News

def home(request):
    data = News.objects.all()
    return render(request, 'home/index.html', {'data': data})

def detail(request, news_id):
    data = get_object_or_404(News, pk=news_id)
    return render(request, 'home/detail.html', {'data': data}) 