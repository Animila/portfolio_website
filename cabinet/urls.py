from django.urls import path
from cabinet.views import cabinet, create, update, delete

app_name = 'cabinet'

urlpatterns = [
    path('', cabinet, name='index'),
    path('create', create, name='create'),
    path('update/<int:news_pk>', update, name='update'),
    path('delete/<int:news_pk>', delete, name='delete'),

]
