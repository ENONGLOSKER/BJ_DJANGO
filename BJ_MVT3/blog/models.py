from django.db import models

# Create your models here.
class tb_post(models.Model):
    img = models.ImageField()
    kategori = models.TextField()
    judul = models.CharField(max_length=255)
    kontent = models.TextField()

    def __str__(self):
        return "{}".format(self.judul)
