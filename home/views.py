from django.shortcuts import render, get_object_or_404

from home.models import News


def home(request):
    context = {
        'data': News.objects.all(),
        'title': 'Главная',
    }
    return render(request, 'home/index.html', context)


def detail(request, news_id):
    context = {
        'data': get_object_or_404(News, pk=news_id),
        'title': 'Статья',
    }
    return render(request, 'home/detail.html', context)






