from django.http import HttpResponse
from django.shortcuts import render
#from .forms import UserForm
from .forms import ContactForm
from .forms import InscriptionForm

def index(request):
    return HttpResponse("En construction")

def inscription(request):


    form = InscriptionForm(request.POST or None)


    if form.is_valid():



        form.save()


    return render(request, 'web/inscription.html', locals())

def login(request):



    return render(request, 'web/login.html', locals())


def contact(request):
     
    
    form = ContactForm(request.POST or None)
    
    if form.is_valid(): 
        
        form.save()

    return render(request, 'web/contact.html', locals())

def condutil(request):

    return render(request, 'web/condutil.html', locals())


def donneeperso(request):

    return render(request, 'web/donneeperso.html', locals())

def menleg(request):
    return render(request, 'web/menleg.html', locals())
