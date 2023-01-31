from django.shortcuts import render

def index(request):
    context ={
        'judul':'HALAMAN HOME'
    }
    return render(request, 'index.html',context)