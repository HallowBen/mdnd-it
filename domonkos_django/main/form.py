from django import forms
from main.models import Rating
from main.models import Contact
from captcha.fields import CaptchaField


class Rateform(forms.ModelForm):
    class Meta:
        model=Rating
        fields=('r_bname','r_sname','r_fname','r_message','rating')


class Contactform(forms.ModelForm):
    class Meta:
        model=Contact
        fields=('c_bname','c_sname','c_fname','c_email', 'c_pnumber','c_message')

class Captcha(forms.Form):
        captcha = CaptchaField()

