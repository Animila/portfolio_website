from django.urls import path
from .views import detail, home, cabinet

app_name = 'home'

urlpatterns = [
    path('', home, name="home"),
    path('<int:news_id>/', detail, name='detail'),
    path('cabinet/', cabinet, name='cabinet'),
]
