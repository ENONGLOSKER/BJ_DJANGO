from django import forms
from .models import blog

# class postForm(forms.Form):
#     judul   = forms.CharField( max_length=20)
#     isi     = forms.CharField( 
#         widget=forms.Textarea()
#     )
#     kategori = forms.CharField(max_length=20)

#     def clean_judul(self):
#         judul_input = self.cleaned_data.get('judul')

#         if judul_input == 'python':
#             raise forms.ValidationError("mohon maaf🙏🏻 tidak bisa menginputkan data pyton!")
#         return judul_input
class postForm(forms.ModelForm):
    class Meta:
        model = blog
        fields = "__all__"