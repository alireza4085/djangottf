# درون فایل forms.py
from django import forms

class PaUpdateForm(forms.Form):
    IDre = forms.IntegerField()
    Ncode = forms.IntegerField()
    Side = forms.CharField(max_length=30)
    fname = forms.CharField(max_length=255)
    lname = forms.CharField(max_length=255)
    dateofbirth = forms.DateField()
    tel = forms.IntegerField()
    email = forms.CharField()
    proficiency = forms.CharField(max_length=255)
    city = forms.CharField(max_length=255)
    street = forms.CharField(max_length=255)
    plaque = forms.IntegerField()