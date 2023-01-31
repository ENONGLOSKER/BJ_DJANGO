from django.shortcuts import render
from blog . models import blogPost

def index(request):
    pos = blogPost.objects.all().order_by('-id')[:3] 
    context = {
        'judul':'PAGE BLOG',
        'post' : pos
    }
    return render(request,'index.html',context)

