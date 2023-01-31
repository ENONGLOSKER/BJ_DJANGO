from django.shortcuts import render

def index(request):

    context = {
        'title': 'DJANGO FORM'
    }
    if request.method == 'POST':
        print('selamat ini adalah method POST')
        context['nama']   =(request.POST['nama'])
        context['alamat'] =(request.POST['alamat'])
    else:
        print('ini adalah method GET')
    return render(request,'index.html',context)
