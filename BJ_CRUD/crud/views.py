from django.shortcuts import render,redirect
from .models import crudModel
from .forms import crudForm

# Create your views here.
def read(request):
    read = crudModel.objects.all().order_by('-id')
    context ={
        'judul':'Page Reade',
        'datas':read
    }
    return render(request, 'crud/read.html',context)

def create(request):
    create=crudForm(request.POST or None)
    if request.method == 'POST':
        if create.is_valid():
            create.save()

        return redirect('index:read')

    context = {
        'judul':'Page Create',
        'datas':create
    }
    return render(request, 'crud/crup.html',context)

def delete(request,delete_id):
    crudModel.objects.filter(id = delete_id).delete()
    return redirect('index:read')

def update(request,up_id):
    update_id = crudModel.objects.get(id=up_id)
    updateForm = {
        'nama' : update_id.nama,
        'ket' : update_id.ket,
        'email' : update_id.email,
    }

    update=crudForm(request.POST or None, initial=updateForm, instance=update_id)
    
    if request.method == 'POST':
        if update.is_valid():
            update.save()

        return redirect('index:read')

    context = {
        'judul':'Page update',
        'datas':update
    }
    return render(request, 'crud/crup.html',context)