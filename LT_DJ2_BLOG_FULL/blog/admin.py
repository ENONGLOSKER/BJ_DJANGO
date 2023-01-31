from django.contrib import admin
from . models import blogPost

# Register your models here.
class blogPostAdmin(admin.ModelAdmin):
    readonly_fields = ['slug','publish','update']
    
admin.site.register(blogPost, blogPostAdmin)
