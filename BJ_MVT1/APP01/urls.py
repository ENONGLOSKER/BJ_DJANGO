from django.urls import path
from . import views

urlpatterns = [  
    path('satu', views.index) #views.index merupakan cara pemanggilan fungsi pada file views
  
]
