"""projeismi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from anasayfa.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('selamlar/', admin.site.urls),
    path("",index,name = "anasayfa_index"),
    path("<int:id>/",ozel,name = "ozel"),
    path("dinamik/<str:id>",dinamik,name="dinamik"),
    path("user/",urun,name="urun"),
    path("zar/",zar,name="zar"),
    path("kullanici/",include("kullanici.urls")),
    path("formornek/",form_ornek,name="form"),
    path("urun/<int:id>",ayrinti_getir,name = "urun"),
    path("form2/",form2,name="form2"),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

