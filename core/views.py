from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib import messages
from product.models import ProductVersion
from core.models import Contact
from core.forms import ContactForm, SubscribeForm
from core.tasks import process_func




def home(request):
    print(request.user.is_authenticated)
    return render(request, 'index.html')

def about(request):
    return render(request, 'about-us.html')


def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        if 'contactform' in request.POST:
            form = ContactForm(data=request.POST)
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS, 'Melumatlar qeyde alindi!')
                return redirect(reverse_lazy('contact'))
    context = {
        'form': form
    }
    return render(request, 'contact.html', context)


def export(request):
    process_func.delay()
    return redirect('/')





 