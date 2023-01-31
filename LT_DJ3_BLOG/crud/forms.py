from django import forms
from  .models import crudModel

class crudForm(forms.ModelForm):
    class Meta:
        model = crudModel
        fields = ['foto','nama','ket','email']