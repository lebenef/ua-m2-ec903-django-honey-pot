from django import forms


class LonginForm(forms.Form):

    username = forms.CharField(max_length=100)

    password = forms.CharField(max_length=100, widget=forms.Passwordinput)

