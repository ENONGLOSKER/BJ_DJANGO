from django.shortcuts import render

def index(request):
    context = {
        'judul':'Home'
    }
    return render(request,'index.html',context)