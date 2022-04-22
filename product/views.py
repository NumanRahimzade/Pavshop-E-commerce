from itertools import product
from pyexpat import model
from unicodedata import category
from django.http import request
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import  ListView
from django.template import context
from .models import *
from product.models import ProductVersion,ProductImages,Product,Category,Brand
from blog.models import Tag
from django.db.models import Count

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


class ProductListView(ListView):
    template_name='product-list.html'
    model= ProductVersion
    context_object_name='products'
    ordering=('-created_at',)
    paginate_by = 3

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['categories']= Category.objects.all()    #Category.objects.filter(products__isnull=False).distinct()
        context['colors']=PropertyValues.objects.all()
        context['tags']=Tag.objects.annotate(chapters_cnt=Count('blog_tags')).order_by('-chapters_cnt')
        context['brands']=Brand.objects.all()
        return context


    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.request.GET.get('category_id') # 1
        color_id=self.request.GET.get('color_id')
        tag_id=self.request.GET.get('tag_id')
        brand_id=self.request.GET.get('brand_id')
        if color_id:
            queryset = queryset.filter(property__propertyname__name='color',property__id=color_id)
        if category_id:
            queryset = queryset.filter(product__category__id=category_id)
        if tag_id:
            queryset=queryset.filter(tags__id=tag_id)
        if brand_id:
            queryset=queryset.filter(product__brand_id=brand_id)
        return queryset





