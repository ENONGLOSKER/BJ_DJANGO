from django.shortcuts import render
from .models import Post
# Create your views here.
def app1(request):
    datas = Post.objects.all()
    context = {
        'data':datas

    }
    return render(request,'app1.html',context)