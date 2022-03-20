from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.home, name="home"),
    path('<int:news_id>/', views.detail, name='detail')
]
