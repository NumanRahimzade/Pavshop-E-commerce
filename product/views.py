from django.shortcuts import render

# Create your views here.

def productdetail(request):
    return render(request,'product-detail.html')

def productlist(request):
    return render(request,'product-list.html')
