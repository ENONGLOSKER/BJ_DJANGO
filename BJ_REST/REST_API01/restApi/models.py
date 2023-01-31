from django.db import models

# Create your models here.
class produkModel(models.Model):
    nama        = models.CharField(max_length=30)
    kategori    = models.CharField(max_length=20)
    harga       = models.DecimalField(max_digits=4, decimal_places=2)
    keterangan  = models.TextField()
    jumlah      = models.IntegerField()

    def __str__(self):
        return self.nama