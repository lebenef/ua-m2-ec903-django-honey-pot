from django.http import HttpResponse
from django.shortcuts import render
from .forms import LoginForm
from .forms import ContactForm

def index(request):
    return HttpResponse("En construction")

def login(request):


    form = LoginForm(request.POST or None)


    if form.is_valid(): 


        username = form.cleaned_data['username']

        password = form.cleaned_data['password']


        envoi = True

    


    return render(request, 'web/login.html', locals())


def contact(request):
     
    
    form = ContactForm(request.POST or None)
    
    if form.is_valid(): 
        sujet = form.cleaned_data['sujet']
        message = form.cleaned_data['message']
        envoyeur = form.cleaned_data['envoyeur']
        
        envoi = True
    return render(request, 'web/contact.html', locals())

def condutil(request):

    return render(request, 'web/condutil.html', locals())


def donneeperso(request):

    return render(request, 'web/donneeperso.html', locals())

def menleg(request):

    return render(request, 'web/menleg.html', locals())
