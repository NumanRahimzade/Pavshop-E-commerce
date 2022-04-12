from django.shortcuts import render
from django.template import context
from .models import *
from product.models import ProductVersion,ProductImages,Product,Category

# Create your views here.

def productdetail(request,id):
    products=ProductVersion.objects.get(id=id)
    images=ProductImages.objects.all()
    mainproduct=ProductVersion.objects.filter(id=id).first()
    # like = mainproduct.category.products.exclude(id=mainproduct.id).order_by('-created_at')[:3]
    like = ProductVersion.objects.filter(product__category=mainproduct.product.category).exclude(id=mainproduct.id).order_by('-created_at')[:3]
    # print(mainproduct.category.products.all())
    context={
        'products':products,
        'images':images,
        'like':like,
        'mainproduct': mainproduct,

    }
    return render(request,'product-detail.html',context)

def productlist(request):
    return render(request,'product-list.html')


