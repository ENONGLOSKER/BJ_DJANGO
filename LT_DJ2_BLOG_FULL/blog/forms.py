from django import forms
from .models import blogPost

class postForm(forms.ModelForm):
    class Meta:
        model  = blogPost
        fields = ['img_header','kategori','judul','isi','foto','nama']
