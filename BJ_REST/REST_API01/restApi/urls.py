from django.urls import path
from . import views

urlpatterns = [
    path('read/',views.readProduk),
    path('readDetail/<int:id>',views.ProdukDetail),
    path('create/',views.createProduk),
    path('update/<int:id>',views.updateProduk),
    path('delete/<int:id>',views.deleteProduk),
]