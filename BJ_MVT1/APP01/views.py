from django.shortcuts import render

# Create your views here.
def index(request):
    context = { #Ini adalah variabel, yang di taruh setelah file html pada render. cara penggunaanya menggunakan {{ key }} yang ditaruh di file html
        'judul':'APP 01',
        'admin':'el132321',
        'appCss': 'app01/css/style2.css',# ini adalalah css yang disimpan di variabel context
    }
    return render(request, 'app01/app1.html', context) 
    #nama sub folder /nama file 