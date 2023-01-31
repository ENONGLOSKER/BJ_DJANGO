from django.shortcuts import render
import requests

def index(request):
    respons = requests.get('https://jsonplaceholder.typicode.com/photos').json()
    context = {
        'datas':respons,
    }
    return render(request,'index.html',context)