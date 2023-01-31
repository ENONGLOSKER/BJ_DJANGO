from django.urls import path
from . import views

urlpatterns = [
    path('monitor/', views.index, name='index'),
]