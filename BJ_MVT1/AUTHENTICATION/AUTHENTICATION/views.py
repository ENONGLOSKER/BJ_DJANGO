from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

def index(request):
    context ={
        'judul':'AUTHENTICATION',
    }
    print(request.user.is_authenticated)
    
    template_name = None

    if request.user.is_authenticated:
        template_name = 'index.html'
    else:
        template_name = 'anonim.html'

    return render(request, template_name, context)


def loginView(request):
    context={
        'judul':'Login',
    }

    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('index')
        else:
            return render(request, 'login.html',context)

    if request.method == 'POST':
       
        username_log = request.POST['username']
        password_log = request.POST['password']

        user = authenticate(request, username=username_log, password=password_log)
        if user is not None:
            login(request, user)

            return redirect('/')
        else:
            return redirect('/login')      

@login_required
def logoutView(request):
    context ={
        'judul':'Logout'
    }
    
    if request.method =='POST':
        if request.POST['logout']=='Submit':
            logout(request)
        return redirect('index')

    return render(request, 'logout.html',context)