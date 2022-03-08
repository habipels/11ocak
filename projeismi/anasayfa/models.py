from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class kategori(models.Model):
    kategori_ismi = models.CharField(max_length=50,verbose_name = "kategori isimi")
    def __str__(self):
        return self.kategori_ismi
class isimler(models.Model):
    categori = models.ForeignKey(kategori, null=True,on_delete = models.CASCADE)
    ogr_isim = models.CharField(max_length=40)
    gorsel = models.FileField(upload_to='kisi_gorsel/',null=True,blank = True,verbose_name="Kişi Fotoğrafı")
    text = models.TextField(max_length=250,null=True)
    aciklama = RichTextField(null=True)
    def __str__(self):
        return self.ogr_isim

class ornek(models.Model):
    isim = models.CharField(max_length=40,verbose_name="İsim Soyisim")
    numara = models.IntegerField()

