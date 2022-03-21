from django.shortcuts import render, get_object_or_404
from .models import Blogs

def blogs(request):
    data = Blogs.objects.all()
    return render(request, 'blogs/list_blogs.html', {'data': data})

def detail(request, blog_id):
    data = get_object_or_404(Blogs, pk=blog_id)
    return render(request, 'blogs/detail.html', {'data': data})