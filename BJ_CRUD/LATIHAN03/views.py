from django.shortcuts import render

def index(request):
    context= {
        'judul':'Page Home',
    }
    return render(request, 'index.html',context)