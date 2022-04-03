from django.http import HttpResponseRedirect
from django.shortcuts import render
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


def redactory(request, news_pk):
    return render(request, 'cabinet/detail.html')


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