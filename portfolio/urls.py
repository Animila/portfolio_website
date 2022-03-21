from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
import home
import blogs
import about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls'), name="home"),
    path('blogs/', include('blogs.urls'), name='blogs'),
    path('about/', include('about.urls'), name='about')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
