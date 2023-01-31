from django.shortcuts import render
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import user_passes_test

# Create your views here.
def index(request):
    context = {
        'judul':'Page Blog'
    }
#cek internal
    ugrup = Group.objects.get(name='penulis')
    agrup =  request.user.groups.all()

    template_name= None
    if ugrup in agrup:
        template_name= 'blog/blog_us.html'
    
    else:
        template_name= 'blog/blog_an.html'

    return render(request,template_name, context)

#cek dengan dekorator
#-----------------------------------------------------
def cekfungsi(user):
    ugrup = Group.objects.get(name='penulis')
    agrup = user.groups.all()

    status = ugrup in agrup
    print(status)
    return status

@user_passes_test(cekfungsi)
def auth1(request):
    context = {
        'judul':'Blog auth 1'
    }
    return render(request,'blog/auth.html', context)
#-----------------------------------------------------

#cek dengan dekorator lambda
#-----------------------------------------------------
@user_passes_test(lambda user:Group.objects.get(name='penulis') in user.groups.all())
def auth2(request):
    context = {
        'judul':'Blog auth 2'
    }
    return render(request,'blog/auth.html', context)
#-----------------------------------------------------
