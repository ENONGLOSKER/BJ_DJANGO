from django.db import models
from django.utils.text import slugify

# Create your models here.
class blogPost(models.Model):
    img_header  = models.ImageField( blank=True, null=True)
    kategori    = models.CharField(max_length=20)
    judul       = models.CharField(max_length=50)
    isi         = models.TextField()
    foto        = models.ImageField(blank=True, null=True)
    nama        = models.CharField(max_length=20)
    publish     = models.DateTimeField(auto_now_add=True)
    update      = models.DateTimeField(auto_now=True)
    slug        = models.SlugField(blank=True, editable=False)

    #slug blog 
    def save(self):
        self.slug = slugify(self.judul)
        super(blogPost, self).save()
    
    def __str__(self):
        return "{},{}".format(self.id, self.judul)
