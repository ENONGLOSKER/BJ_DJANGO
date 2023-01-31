from django.shortcuts import render
from .forms import postForm
from .models import blog
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    blogs = blog.objects.all()
    context={
        'judul':'HALAMAN BLOG',
        'datas':blogs,
    }
    return render(request, 'blog/index.html',context)

def datain(request):
    post_form = postForm(request.POST or None) #ini untuk validasi data agar tidak duplikat juga untuk form kosong
    if request.method == 'POST':
        if post_form.is_valid():
            post_form.save()
        return HttpResponseRedirect('/blog/')
    # error = None
    # if request.method == 'POST':
    #     if post_form.is_valid(): #validasi form
    #         blog.objects.create(   
    #                 # judul       = request.POST.get('judul'), ini untuk data tanpa validasi
    #                 judul         = post_form.cleaned_data.get('judul'), #ini untuk data yang sudah di validasi
    #                 # isi         = request.POST.get('isi'),
    #                 isi           = post_form.cleaned_data.get('isi'),
    #                 # kategori    = request.POST.get('kategori'),             
    #                 kategori      = post_form.cleaned_data.get('kategori'),             
    #             )
    #         return HttpResponseRedirect ('/blog/')
    #     else:
    #         error = post_form.errors
     
    context={
        'judul':'HALAMAN INPUT DATA',
        'posts':post_form,
        # 'error':error,
    }
   

    return render(request, 'blog/datain.html',context)