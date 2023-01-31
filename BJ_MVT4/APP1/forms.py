from django import forms
# Create your views here.
class app1_kontak (forms.Form):
    # tipe angka
    integerfield = forms.IntegerField(
        label='Nomor HP',
        min_value=11,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'masukan nomor hp'
            }
        )
    )
    decimalfied = forms.DecimalField(required=False)
    floatfield = forms.FloatField(label='angka bersisa')
    boolanfield = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={
                'class':'form-check-input'
            }
        )
    )
    charfield = forms.CharField(max_length=20)
    # tipe hurup
    emailfield = forms.EmailField()
    # regexfield = forms.RegexField(required=False)
    slugfield = forms.SlugField()
    urlfield = forms.URLField()
    ipfield = forms.GenericIPAddressField()
    #select input
    pilih =(
        ('nilai1','PILIHAN1'),
        ('nilai2','PILIHAN2'),
        ('nilai3','PILIHAN3'), 
    )
    choisfield = forms.ChoiceField(
        choices=pilih,
        widget=forms.RadioSelect(
           attrs={
            'class':'form-check-input'
           }
        )
        )    
    multipele_choisfield= forms.MultipleChoiceField(choices=pilih)
    multipele_type_choice = forms.TypedMultipleChoiceField(choices=pilih)
    nuul_booleanfield = forms.NullBooleanField()
    #data time
    date_field = forms.DateField()
    datetime_field = forms.DateTimeField()
    durationfield = forms.DurationField()
    timefield = forms.TimeField()
    splitdatetime_field = forms.SplitDateTimeField()
    #file input
    file_filed = forms.FileField()
    img_field =forms.ImageField( )

    # WIGET -------------------
    wiget_pilih = forms.ChoiceField(
        widget=forms.RadioSelect(),
        choices=pilih)
    wiget_alamat = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class':'form-control'
            }
        ),
        max_length=20)

    th = range(1945,2024)
    widget_date = forms.DateField(
        widget=forms.SelectDateWidget(
            years=th,
            attrs = {
                'class':'form-control col-sm-2',
            }
            )
    )