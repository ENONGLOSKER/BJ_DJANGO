from django.shortcuts import render
from . models import monitor

# Create your views here.
def index(request):
    datas = monitor.objects.all()
    context = {
        'judul':'EMPLOYES MONITORING',
        'datas': datas,
    }
    return render(request, 'monitor/index.html',context)