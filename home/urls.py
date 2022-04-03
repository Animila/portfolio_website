from django.urls import path
from .views import detail, home, about


app_name = 'home'

urlpatterns = [
    path('', home, name="home"),
    path('<int:news_id>/', detail, name='detail'),
    path('about/', about, name='about'),
]
