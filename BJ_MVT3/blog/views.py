from django.shortcuts import render
from .models import tb_post
from django.http import HttpResponse

# Create your views here.
def index(request):
    info = tb_post.objects.all()
    context = {
        'judul1' : 'BELAJAR ',
        'judul2' : 'DJANGO',
        'datas' : info
    }
    return render(request, 'blog/index.html',context)
