from django.shortcuts import render

def index(request):

    context = {
        'judul':'Page Home',
        'salam':'selamat datang di page home'
    }
    return render(request,'index.html',context)