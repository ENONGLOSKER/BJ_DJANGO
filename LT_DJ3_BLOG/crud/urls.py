from django.urls import path
from .import views
app_name = 'crud'

urlpatterns = [
    path('',views.read,name='read'),
    path('create',views.create,name='create'),
    path('delete<int:delete_id>',views.delete,name='delete'),
    path('update<int:up_id>',views.update,name='update'),
] 