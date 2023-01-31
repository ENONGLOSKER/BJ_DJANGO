from django.shortcuts import render
from django.views import View

def index(request):
    context = {
        'judul': 'FUNCTION BASE',
    }
    if request.method == 'POST':
        context ['judul'] = 'Fuction Base View'
    return render(request,'index.html',context)

class indexClass(View):
    template_name = ''
    context = {}

    def get(self,request):
        self.context['judul'] = 'GET Class Base View'
        return render(request, self.template_name,self.context)
    
    def post(self,request):
        self.context['judul'] = 'POST Class Base View'
        return render(request, self.template_name, self.context)