from django import forms
from .models import ornek
class moedel_form(forms.ModelForm):
    class Meta:
        model = ornek
        fields = ["isim","numara"]
