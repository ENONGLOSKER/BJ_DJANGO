from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='blog'),
    path('auth1',views.auth1, name='auth1'),
    path('auth2',views.auth2, name='auth2'),
]
