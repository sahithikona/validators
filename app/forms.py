from django import forms
from django.core import validators
def check(sname):
    if sname[0].lower()=="s":
        raise forms.ValidationError("name starts with s")

    

class Studentform(forms.Form):
    sname=forms.CharField(max_length=100,validators=[check])
    sage=forms.IntegerField()
    sid=forms.IntegerField()
    semail=forms.EmailField()
    remail=forms.EmailField()
    bot=forms.CharField(max_length=100,widget=forms.HiddenInput,required=False)
    mobile=forms.CharField(max_length=10,validators=[validators.MinLengthValidator(10),validators.RegexValidator("[6-9]\d{9}")])

    def clean(self):
        em=self.cleaned_data["semail"]
        rem=self.cleaned_data["remail"]
        name=self.cleaned_data["sname"]
        
        if em!=rem or len(name)<5:
            raise forms.ValidationError("invalid ")
    def clean_bot(self):
         b=self.cleaned_data["bot"]
         if len(b)>0:
            raise forms.ValidationError("bot")
        
        



    
