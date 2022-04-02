from django.urls import path
from .views import detail, home

app_name = 'home'

urlpatterns = [
    path('', home, name="home"),
    path('<int:news_id>/', detail, name='detail'),
]
