from django.shortcuts import render
from .models import kontenModel

# Create your views here.
def blog(request):
    posting2 = kontenModel.objects.all()
    context={
        'judul':'BLOG', 
        'pos':posting2,

    }
    return render (request,'blog.html',context)