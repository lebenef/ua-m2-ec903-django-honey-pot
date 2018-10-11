from django import forms


class LoginForm(forms.Form):

    username = forms.CharField(max_length=100)

    password = forms.CharField(max_length=100, widget=forms.PasswordInput)


class ContactForm(forms.Form):
    sujet = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    envoyeur = forms.EmailField(label="Votre adresse e-mail")
