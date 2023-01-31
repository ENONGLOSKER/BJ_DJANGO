from django.db import models

# Create your models here.
class blog(models.Model):
    judul    = models.CharField(max_length=20)
    isi      = models.TextField()
    kategori = models.CharField(max_length=20)

    updated  = models.DateTimeField(auto_now_add=True)
    publisted= models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{},{}".format(self.id, self.judul)