from django.http import HttpResponse
from django.shortcuts import render
from .forms import LoginForm


def index(request):
    return HttpResponse("En construction")

def login(request):


    form = LoginForm(request.POST or None)


    if form.is_valid(): 


        username = form.cleaned_data['username']

        password = form.cleaned_data['password']


        envoi = True

    


    return render(request, 'web/login.html', locals())
