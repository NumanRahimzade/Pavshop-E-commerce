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
            # return redirect('home')
    return {'subscribe_form': subscribe_form}