from django.http import HttpResponse
from django.shortcuts import render
#from .forms import UserForm
from .forms import ContactForm
from .forms import LoginForm
from .forms import DataForm
from django.utils import timezone

def index(request):
    return HttpResponse("En construction")


def login(request):

    ip = request.META.get('REMOTE_ADDR')
    useragent = request.META['HTTP_USER_AGENT']
    date = timezone.now()

    form = LoginForm(request.POST or None)
    if form.is_valid():
        form.save()
   
    form2 = DataForm(request.POST or None, initial={'addressip':ip,'useragent':useragent,'datetime':date})
    if form2.is_valid():
        form2.save()

    return render(request, 'web/login.html', locals())


def contact(request):
     
    ip = request.META.get('REMOTE_ADDR')
    useragent = request.META['HTTP_USER_AGENT']
    date = timezone.now()

    form = ContactForm(request.POST or None)    
    if form.is_valid():        
        form.save()


    form2 = DataForm(request.POST or None,initial={'addressip':ip,'useragent':useragent,'datetime':date})
    if form2.is_valid():
        form2.save()

    return render(request, 'web/contact.html', locals())

def condutil(request):

    return render(request, 'web/condutil.html', locals())


def donneeperso(request):

    return render(request, 'web/donneeperso.html', locals())

def menleg(request):
    return render(request, 'web/menleg.html', locals())
