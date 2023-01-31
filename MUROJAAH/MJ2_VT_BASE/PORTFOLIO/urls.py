from django.contrib import admin
from django.urls import path,include
from .views import index
from django.conf import settings #01 tambahkan ini, agar img terbaca di templates
from django.conf.urls.static import static #02 tambahkan ini, agar img terbaca di templates


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name='home'),
    path('app/',include('app.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #03 tambahkan ini, agar img terbaca di templates

