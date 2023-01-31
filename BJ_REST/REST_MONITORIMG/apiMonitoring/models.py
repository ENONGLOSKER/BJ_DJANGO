from django.db import models

# Create your models here.
class apiModel(models.Model):
    nama_projek     = models.CharField(max_length=20) 
    lead            = models.CharField(max_length=20)
    foto            = models.ImageField(upload_to='img', null=True  )
    nama            = models.CharField(max_length=20)
    email           = models.EmailField()
    progress        = models.IntegerField()

    def __str__(self):
        return self.nama_projek
