
from django.contrib import admin
from django.urls import path,include
from . import views #untuk menyambungkan file views dengan file ini
# from APP01 import views as viewsapp1  #untuk menyambungkan file views pada app dengan file ini

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index), #views.index merupakan cara pemanggilan fungsi pada file views
    path('menu/', views.menu),
    path('app1/', include('APP01.urls')),
    # path('app1/', viewsapp1.index) #viewsapp1.index merupakan cara pemanggilan fungsi pada file views di app

    
]
