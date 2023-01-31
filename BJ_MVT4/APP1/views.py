from django.shortcuts import render
from . forms import app1_kontak

def index(request):
    app1_form = app1_kontak()
    context ={
        'judul':'form app1',
        'kontak':app1_form
    }
    print(request.POST)
    if request.method == 'POST':
        context ['nama'] = request.POST ['nama']
        context ['alamat'] = request.POST ['alamat']
    else:
        print('ini methiod GET bro!')
    return render(request, 'app1/index.html',context)
