from django.contrib import admin
from django.urls import path
from .views import *

app_name = "user"

urlpatterns = [
    path("giris/",kullanici_giris,name="giris"),
    path("kayit/",kulanici_kayit,name="kayit"),
    path("cikis/",kullanici_cikis,name="cikis"),
]

