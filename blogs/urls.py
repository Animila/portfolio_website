from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns = [
    path('', views.blogs, name="all_blogs"),
    path('<int:blog_id>/', views.detail, name='detail')
]
