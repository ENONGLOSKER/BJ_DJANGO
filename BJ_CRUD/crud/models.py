from django.db import models

# Create your models here.
class crudModel(models.Model):
    nama    = models.CharField(max_length=20)
    ket     = models.TextField()
    email   = models.CharField(max_length=20)
    update  = models.DateTimeField(auto_now_add=True)
    publish = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nama
