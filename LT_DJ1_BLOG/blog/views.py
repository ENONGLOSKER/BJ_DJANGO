from django.shortcuts import render
from .models import tb_post
from .forms import blogForms

# Create your views here.
def blog(request):
    info = tb_post.objects.all()
    categoris = tb_post.objects.values('categori').distinct()
    context = {
        'judul':'Page Blog',
        'salam':'Selamat Datang di Page Blog',
        'categoris': categoris,
        'datas': info
    }
    return render(request, 'blog/blog.html',context)

def blogCategori(request,categori_url):
    info = tb_post.objects.filter(categori=categori_url)
    categoris = tb_post.objects.values('categori').distinct()
    context = {
        'judul':'Page Blog Categori',
        'salam':'Selamat Datang di Blog Categori',
        'categoris': categoris,
        'datas': info
    }
    return render(request,'blog/blogCategori.html',context)

def blogDetail(request,slug_url):
    info = tb_post.objects.get(slug=slug_url)
    categoris = tb_post.objects.values('categori').distinct()
    context = {
        'judul':'Page Blog Detail',
        'salam':'Selamat Datang di Page Blog Detail',
        'categoris': categoris,
        'datas': info
    }
    return render(request,'blog/blogDetail.html',context)

def create(request):

    postingan = blogForms(request.POST or None)
    if request.method == 'POST':
        if postingan.is_valid:
            postingan.save()
    
    context = {
        'postingan' : postingan
    }
    return render(request, 'blog/create.html',context)