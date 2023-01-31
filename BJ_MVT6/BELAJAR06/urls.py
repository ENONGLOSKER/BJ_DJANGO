
from django.contrib import admin
from django.urls import path
from .views import index, indexClass

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('class', indexClass.as_view(template_name='index2.html'))
]
