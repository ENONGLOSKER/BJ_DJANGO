from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'judul':'Home',
    }
    return render(request,'index.html',context)