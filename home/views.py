from django.shortcuts import render, get_object_or_404
from .models import News
from django.contrib.admin.views.decorators import staff_member_required

def home(request):
    context = {
        'data': News.objects.all(),
        'title': 'Главная',
    }
    return render(request, 'home/index.html', context)


@staff_member_required
def cabinet(request):
    context = {
        'title': 'Кабинет',
    }
    return render(request, 'home/cabinet.html', context)


def detail(request, news_id):
    context = {
        'data': get_object_or_404(News, pk=news_id),
        'title': 'Статья',
    }
    return render(request, 'home/detail.html', context)
