from django.shortcuts import render
from django.template import context
from product.models import ProductVersion,ProductImages

# Create your views here.

def productdetail(request):
    products=ProductVersion.objects.all()
    images=ProductImages.objects.all()
    context={
        'products':products,
        'images':images

    }
    return render(request,'product-detail.html',context)

def productlist(request):
    return render(request,'product-list.html')
