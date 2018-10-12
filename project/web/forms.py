from django.forms import ModelForm
from django import forms
from .models import User
from .models import Contact

class InscriptionForm(forms.ModelForm):
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
