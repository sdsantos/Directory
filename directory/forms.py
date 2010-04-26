from django.forms import ModelForm
from django import forms
from models import Company
from captcha.fields import CaptchaField

class CompanyForm(ModelForm):
    class Meta:
        model = Company
        exclude = ('approved',)
    
    captcha = CaptchaField()