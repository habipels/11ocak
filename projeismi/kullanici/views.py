from django.shortcuts import render ,HttpResponse ,redirect
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from .form import *
# Create your views here.
def kullanici_giris(request):
    form = LoginForm(request.POST or None)
    context = {
        "formornek":form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username = username,password = password)
        if user is None:
            #messages.info(request,"Kullanıcı Adı veya Parola Hatalı")
            return render(request,"form2.html",context)
        login(request,user)
        return redirect("anasayfa_index")
    return render(request,"form2.html",context)
def kulanici_kayit(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        email = form.cleaned_data.get("email")
        newUser = User(username =username,email=email)
        newUser.set_password(password)
        newUser.save()
        login(request,newUser)
        return redirect("anasayfa_index")
    context = {
            "formornek" : form
        }
    return render(request,"form2.html",context)
def kullanici_cikis(request):
    logout(request)
    return redirect("anasayfa_index")
