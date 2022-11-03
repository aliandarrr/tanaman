from django.db import models

# Create your models here.
class data(models.Model):
    email = models.CharField(max_length=100, default="")
    password = models.CharField(max_length=100, default="")
    
class bunga(models.Model):
    nama = models.CharField(max_length=100, default="")
    nama_latin = models.CharField(max_length=100, default="")
    images = models.ImageField(upload_to="static/images", null=True)
    cara_perawatan = models.CharField(max_length=500, default="")
    jenis_tanaman = models.CharField(max_length=100, default="")
    jumlah = models.IntegerField(null=True)