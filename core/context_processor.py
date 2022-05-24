from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import SubscribeForm
from django.contrib import messages


def subject_renderer(request):
    subscribe_form = SubscribeForm()
    if request.method == 'POST' and 'subscribe' in request.POST:
        subscribe_form = SubscribeForm(data=request.POST)
        if subscribe_form.is_valid():
            subscribe_form.save()
            messages.add_message(request, messages.SUCCESS, 'Email qeyde alindi!')
            # return redirect('.')
        else:
            messages.add_message(request, messages.WARNING, 'Daxil edilen email teleblere uygun deyil veya email artiq qeydiyyatdan kecmisdir!')
    return {'subscribe_form': subscribe_form}