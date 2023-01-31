from django.contrib import admin
from django.urls import path,include
from .import views
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path ('admin/', admin.site.urls),
    path ('',views.index, name='index'),
    path ('login',views.loginView, name='login'),
    path ('logout',views.logoutView, name='logout'),
    path ('blog/',include('BLOG.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

