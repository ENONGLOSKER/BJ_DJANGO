from django.shortcuts import render

# Create your views here.
def app(request):
    context = {
        'judul':'APP'
    }
    return render(request, 'app/app.html',context)