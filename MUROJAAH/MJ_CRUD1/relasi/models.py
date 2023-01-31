from django.db import models

# Create your models here.
class kategoriModel(models.Model):
    jenis = models.CharField(max_length=100)
    
    def __str__(self):
        return self.jenis

class kontenModel(models.Model):
    foto    = models.ImageField(upload_to='')
    kategori= models.ManyToManyField(kategoriModel, related_name='kategori')
    judul   = models.CharField(max_length=100)
    isi     = models.TextField()
    tag     = models.CharField(max_length=100)

    def __str__(self):
        return self.judul

 
