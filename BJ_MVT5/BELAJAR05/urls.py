from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='blog'), #home
    path('blog/',include('blog.urls', namespace='input')), 
]
