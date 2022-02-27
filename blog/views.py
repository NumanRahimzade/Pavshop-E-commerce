from django.shortcuts import render
from django.http import HttpResponse


def blog_list(request):
    return render(request, 'blog-list.html')


def blog_detail(request):
    return render(request, 'blog-detail.html')