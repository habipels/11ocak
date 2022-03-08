from django.shortcuts import render,redirect
from .models import *
from .form import *
# Create your views here.
def index(request):
    cate = kategori.objects.all()
    isim = isimler.objects.all()
    return render(request, "index.html",{"veri":isim,"cate":cate})
def ozel(request,id):
    cate = kategori.objects.all()
    isim = isimler.objects.filter(categori_id = id)
    return render(request, "index.html",{"veri":isim,"cate":cate})
def dinamik(request,id):
    bir = id
    sozluk = {"sira":bir}
    return render(request, "dinamik_url.html",sozluk)

def urun(request):
    return render(request, "kisi.html")

def zar(request):
    import random
    liste_id = []
    kisiler = isimler.objects.all()
    for i in kisiler:
        liste_id.append(i.id)
    ornek_id = random.choice(liste_id)
    kisiler = isimler.objects.filter(id = ornek_id)
    return render(request,"kisi.html",{"z":kisiler})

def form_ornek(request):
    if request.POST.get("isim") and request.POST.get("numara"):
        ornek.objects.create(isim=request.POST.get("isim"),numara = request.POST.get("numara"))
    return render(request, "form.html")

def form2(request):

    formornek2 = moedel_form(request.POST or None,request.FILES or None)
    if formornek2.is_valid():
        article = formornek2.save(commit=False)
        article.save()
        return redirect("anasayfa_index")
    return render(request, "form2.html",{"formornek":formornek2})


def ayrinti_getir(request,id):
    z = isimler.objects.filter(id = id)
    return render(request, "urun_ayrinti.html",{"urun":z})