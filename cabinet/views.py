from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse

from home.models import News
from cabinet.forms import NewsForm


@staff_member_required
def cabinet(request):
    context = {
        'title': 'Кабинет',
        'data': News.objects.order_by('-time'),
    }

    return render(request, 'cabinet/index.html', context)

@staff_member_required
def create(request):
    if request.method == 'POST':
        data = NewsForm(data=request.POST, files=request.FILES)
        if data.is_valid():
            data.save()
            return HttpResponseRedirect(reverse('cabinet:index'))
    else:
        data = NewsForm()
    context = {
        'title': 'Создание',
        'form': data
    }
    return render(request, 'cabinet/create.html', context)

@staff_member_required
def update(request, news_pk):
    data = get_object_or_404(News, pk=news_pk)
    if request.method == 'POST':
        try:
            form = NewsForm(request.POST, instance=data, files=request.FILES)
            form.save()
        except ValueError:
            print('ошибка')
    else:
        form = NewsForm(instance=data)
    context = {
        'data': data,
        'form': form,
        'title': 'Новости',
    }
    return render(request, 'cabinet/detail.html', context)

@staff_member_required
def delete(request, news_pk):
    data_news = get_object_or_404(News, pk=news_pk)
    if request.method == 'POST':
        data_news.delete()
        return HttpResponseRedirect(reverse('cabinet:index'))