from django.shortcuts import render,redirect
from .forms import postForm
from .models import blogPost

# Create your views here.
def blog(request):
    pos   = blogPost.objects.all().order_by('-id')
    context ={
        'judul' : 'Halaman Blog',
        'post' : pos,
       
    }
    return render(request, 'blog/blog.html',context)

def categori(request,categori_id):
    categoriss = blogPost.objects.filter(kategori=categori_id)
    categori_dt = blogPost.values('kategori').distinct() #distinct, digunakan untuk mengambil data khusus atau data yang tidak sama
    context = {
        'categoriss':categoriss,
        'categori_dt':categori_dt,
    }
    return render(request,'blog/blogDetail.html',context)

def blogDetail(request,slug_url):
    info      = blogPost.objects.get(slug=slug_url)
    categori  = blogPost.objects.values('kategori').distinct()
    recentPos = blogPost.objects.all().order_by('-id')[:9] 

    context = {
        'judul':'PAGE BLOG DETAIL',
        'datas':info,
        'categori_dt':categori,
        'recent': recentPos,
    }
    return render(request,'blog/blogDetail.html',context)

def master(request):
    datas = blogPost.objects.all().order_by('-id')

    context = {
        'judul':'PAGE MASTER',  
        'datas':datas,     
    }

    return render(request,'blog/master.html',context)

def delete(request,delete_id):
    blogPost.objects.filter(id=delete_id).delete()
    return redirect('blog:master')

def create(request):
    add_form = postForm(request.POST or None)
    if request.method == 'POST':
        add_form = postForm(request.POST, request.FILES)
        if add_form.is_valid():
            add_form.save()
        return redirect('blog:master')

    context = {
        'judul':'Page Add',
        'datas':add_form
    }
    return render(request, 'blog/create.html',context)

def update(request,up_id):
    update_id = blogPost.objects.get(id=up_id)
    updateForm = {
        'img_header' : update_id.img_header,
        'kategori'   : update_id.kategori,
        'judul'      : update_id.judul,
        'isi'        : update_id.isi,
        'foto'       : update_id.foto,
        'nama'       : update_id.nama,
    }
    add_form = postForm(request.POST or None,request.FILES or None, initial=updateForm, instance=update_id)
   
    if request.method == 'POST':
        if add_form.is_valid():
            add_form.save()
        return redirect('blog:master')

    context = {
        'judul':'Page update',
        'datas': add_form
    }
    return render(request, 'blog/create.html',context)
    