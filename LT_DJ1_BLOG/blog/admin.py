from django.contrib import admin
from . models import tb_post

# Register your models here.
class tb_postAdmin(admin.ModelAdmin):
    readonly_fields = ['slug','publish','update']

admin.site.register(tb_post,tb_postAdmin)

