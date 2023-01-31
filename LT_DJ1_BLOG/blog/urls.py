from django.urls import path
from .import views
app_name = 'blog'

urlpatterns = [
    path('',views.blog,name='blg'),
    path('create/',views.create,name='create'),
    path('post/<str:slug_url>',views.blogDetail, name="detail"),
    path('categori/<str:categori_url>',views.blogCategori,name="categori")
]