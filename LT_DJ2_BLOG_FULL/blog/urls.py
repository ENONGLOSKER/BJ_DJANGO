from django.urls import path
from . import views
app_name ='blog'

urlpatterns = [
    path('',views.blog, name='blog'),
    path('categori/<int:categori_id>',views.categori, name='categori'),
    path('delete/<int:delete_id>',views.delete, name='delete'),
    path('update/<int:up_id>',views.update, name='update'),
    path('create',views.create, name='create'),
    path('master',views.master, name='master'),
    path('post/<str:slug_url>',views.blogDetail, name="detail"),
]