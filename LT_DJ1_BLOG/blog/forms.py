from django import forms
from .models import tb_post

class blogForms(forms.ModelForm):
    class Meta:
        model = tb_post
        fields = "__all__"