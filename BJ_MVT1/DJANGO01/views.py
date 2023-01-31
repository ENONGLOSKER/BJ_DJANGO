
from django.shortcuts import render


def index(request):
   
    return render(request,'index.html')

def menu(request):
    context ={
        'pjCss':'/static/css/style.css'
    }
    return render(request,'menu.html',context)
