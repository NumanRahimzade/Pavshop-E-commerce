from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib import messages

from core.models import Contact
from core.forms import ContactForm, SubscribeForm


def home(request):

    return render(request, 'index.html')

def about(request):
    return render(request, 'about-us.html')


def contact(request):
    form = ContactForm()
    if request.method == 'POST' and 'contactform' in request.POST:
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Melumatlar qeyde alindi!')
            return redirect(reverse_lazy('contact'))
    context = {
        'form': form
    }
    return render(request, 'contact.html', context)



 