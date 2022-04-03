from django.urls import path
from cabinet.views import cabinet, create, redactory

app_name = 'cabinet'

urlpatterns = [
    path('', cabinet, name='index'),
    path('<int:news_pk>', redactory, name='detail'),
    path('create', create, name='create'),
]