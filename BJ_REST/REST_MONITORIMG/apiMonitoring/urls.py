from django.urls import path
from . import views

urlpatterns = [
    path('read/',views.readall),
    path('readdetail/<int:id>',views.readdetail),
    path('create/',views.create),
    path('update/',views.update),
    path('delete/<int:id>',views.delete),
]