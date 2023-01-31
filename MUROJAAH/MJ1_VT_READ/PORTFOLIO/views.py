from django.shortcuts import render

def index(request):
    context = {
        'judul':'HOME'
    }
    return render(request, 'index.html',context)