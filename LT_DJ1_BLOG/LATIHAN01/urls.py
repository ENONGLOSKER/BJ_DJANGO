from django.contrib import admin
from django.urls import path,include
from .import views
from django.conf import settings #01 tambahkan ini, agar img terbaca di templates
from django.conf.urls.static import static #02 tambahkan ini, agar img terbaca di templates

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('blog/',include('blog.urls',  namespace='blog')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #03 tambahkan ini, agar img terbaca di templates
