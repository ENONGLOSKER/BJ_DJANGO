from django.db import models

# Create your models here.
class monitor(models.Model):
    project     = models.CharField(max_length=200)
    lead        = models.CharField(max_length=200)
    foto        = models.ImageField(upload_to='')
    nama        = models.CharField(max_length=200)
    email       = models.EmailField()
    start       = models.DateField()
    end         = models.DateField()
    progres     = models.IntegerField(max_length=100)
    hp          = models.CharField(max_length=200)
    publish     = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.project
