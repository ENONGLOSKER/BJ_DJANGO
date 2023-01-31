## BELAJAR DJANGO WITH RIZQA -------------------

-INSTALASI
python*
env : python -m venv env *
aktivasi env *
django : pip install django*

-BUAT PROJECT
membuat project : dajngo-admin startproject namaapk *
menjalankan project : cd namaapk, py manage.py runserver*
membuat apps : py manage.py startapp namaapk*

-DESAIN DJANGO (MVT)
views :tempat mengontrol isi template
    fungsi, variabel context, queryset
url : tempat alamat template
    alamat utama(project), alamat sub(apps)
templates : tempat tampilan
    setings, inheriten, base tempates
static : tempat file css,js foto/file
    seting, daftar url utama
## ----------------
-SETTING
MEDIA_URL = '/img/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/img')

STATICFILES_DIRS = [
    # BASE_DIR / 'static',
    os.path.join(BASE_DIR, 'static')

]

-URLS
from django.conf import settings 
from django.conf.urls.static import static 


+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 


## ----------------

## -MODEL
field
tipedata
admin
slug
relasi tabel
queryset

## -FORM
crete
read
update
delete

## -AUTHE
login
logout
register

## -AUTHO
permission
session
jwt

## -REST
crud
authe
autho







## ---------------------------------------------