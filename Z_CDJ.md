------------------------------------------------
#BELAJAR DJANGO
-CRUD
-AUTHENTICATION
-AUTHORIZATION
-PYMENT GETWAY
#PROJECT
-MANAJEMEN KARYAWAN
-MANAJEMEN RUMAH SAKIT
-BLOG
-CHAT BOOT
-PEMESANAN
-ECOMERS

------------------------------------------------
01 MEMBUAT DAN MENJALANKAN  ENV
python -m venv env
env\Scripts\activate

02 INSTALL DJANGO
pip install django

03 MEMBUAT PROJECT 
django-admin startproject mysite

STRUKTUR FOLDER
Direktori mysite/ adalah root direktori yang berisi seluruh file dari project. Nama direktori ini bisa diganti dengan apa saja, karena tidak akan jadi masalah bagai Django.
File manage.py adalah program untuk mengelola project Django. saat ingin melakukan sesuatu terhadap project, misalnya: menjalankan server, melakukan migrasi, menciptakan sesuatu, dll.
File mysite/__init__.py adalah sebuah file kosong yang menyatakan direktori ini adalah sebuah paket (python package).
File mysite/settings.py adalah tempat kita mengkonfigurasi project.
File mysite/urls.py adalah tempat kita mendeklarasikan URL.
File mysite/wsgi.py adalah entri point untuk WSGI-compatible

-CARA KERJA DJANGO : HTTP REQUEST -> URL -> VIEWS -> (MODEL*jika butuh data) -> TEMPLATES -> HTTP RESPONSE

04 MENJALANKAN DAN MIGRASI SERVER 
python manage.py runserver
python manage.py migrate

05 MEMBUAT SUPER USER
python manage.py createsuperuser

06 LOGIN ADMIN
http://127.0.0.1:8000/admin

07 MEMBUAT APPS
python manage.py startapp blog

08 MENAMBAH GAMBAR
-buat folder static dan taruh gambah yang akan di tmpilkan.
-panggil dengan alamat src="/static/app01/YTFLASK.png" atau bisa menggunakan 
-{% load static %} taruh di atas tag html paling atas kemudian panggil src="{% static '/app01/YTFLASK.png ' %}"

09 MENGGUNAKAN INCLUDE HTML

-buat folder snippets di templates
-buat file html per bagian yang akan di includkan
-kemudian panggil di file htmlnya dengan sesuai dengan posisi bagian tersebut.
{%include "nama file.html"%}

10 QUERY SET 
menampilkan semua data 
-namaTabel.objects.all()
tb_blog.objects.all()

-menampilkan satu jenis data tertentu
tb_blog.objects.get(id=1)

-menampilkan data tertentu yang sesuai dengan karakter
tb_blog.objects.get(judul__iexact='DjaNgo')

-menampilkan banyak jenis data tertentu
tb_blog.objects.filter (kategori='django')

-menampilkan data dengan urutan tertentu
tb_blog.objects.oerder_by ('judul') #dari a-z
tb_blog.objects.oerder_by ('judul') #dari z-a

-menampilkan data selain yang di kecualikan
tb_blog.objects.exclude (kategori='gosip')

menambah data
-namaTabel.objects.create(namafield='isi1',namafield='isi2')
tb_blog.objects.create(judul='flask',isi='belajar flask')

merubah data 
-jenis dictionary menjadi list
semuaData = tb_blog.objects.all()
semuaData.values_list('id') #konversi ke list

#11 SLUG
#12 NAMEING URL
-cara membuat name, bertujuan agar url yang digunakan lebih flexsibel.
name="index"
-cara menggunakan nya
{% url "index" %}
path('',views.blog,name='blg'),

-cara membuat namespace, digunakan ketika url memiliki sub. ditaruh di dalam kurung include pada url.
namespace = "blog"
path('blog/',include('blog.urls',  namespace='blog'))

-cara menggunakanya
{%url "blog:index"%}

-jika menggunakan parameter maka seperti berikut :
{%url 'blog:categori' categori_url=data.categori%}

categori_url: dari nama parameternya
data : dari varriabel loopingnya
categor : dari field yang ditangkap

-juga kita harus mendefinisikan nama app di url app dengan
app_name = 'blog'

## --------------------------------------------------

#GITHUB
-git init
-git remote
------------ (saat melkukan perubahan/ update mulai dari sini)
-git add
-git commit
-git puhs


- git remote
git remote add origin link repo
git remote add origin https://github.com/ENONGLOSKER/DJANGO.git

- ganti remote git
git remote set-url origin link repo
git remote set-url origin https://github.com/ENONGLOSKER/DJANGO.git
## --------------------------------------------------
home
form registert 
set user and pass
login system
logout system

## --------------------------------------------------
-AUTHENTICATIONS
BASIC*
    login
    logout
    passord change
    password reset
    register new user
TOKEN
REMOTE USER
SESSION
DJANGO REST
CUSTOM
JWT
DJOSER LIBRARY

## --------------------------------------------------



