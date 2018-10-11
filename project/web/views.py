from .forms import ContactForm


def contact(request):


    form = ContactForm(request.POST or None)


    if form.is_valid(): 


        username = form.cleaned_data['username']

        passworr = form.cleaned_data['password']


        envoi = True

    

    # Quoiqu'il arrive, on affiche la page du formulaire.

    return render(request, 'view.html', locals())
