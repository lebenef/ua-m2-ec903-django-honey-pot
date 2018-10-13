from django.forms import ModelForm
from django import forms
from .models import User
from .models import Contact
from .models import Data


class LoginForm(forms.ModelForm):
    class Meta:

        model = User
        
        widgets = {
        'password': forms.PasswordInput(),
        }

        fields = '__all__'


class ContactForm(forms.ModelForm):
    class Meta:

        model = Contact

        fields = '__all__'


class DataForm(forms.ModelForm):
    class Meta:

        model = Data

        widgets = {'addressip': forms.HiddenInput(),'useragent': forms.HiddenInput(),'datetime': forms.HiddenInput()}

        fields = '__all__'

