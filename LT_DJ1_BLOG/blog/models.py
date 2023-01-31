from django.db import models
from django.utils.text import slugify

# Create your models here.
class tb_post(models.Model):
    judul = models.CharField(max_length=255)
    body = models.TextField()
    categori = models.CharField(max_length=255)
    publish = models.DateTimeField(auto_now_add=True)
    update = models.DateField(auto_now=True)
    slug = models.SlugField(blank=True, editable=False)

    #slug blog 
    def save(self):
        self.slug = slugify(self.judul)
        super(tb_post, self).save()
    
    def __str__(self):
        return "{},{}".format(self.id, self.judul)
    