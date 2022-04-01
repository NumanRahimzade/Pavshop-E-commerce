from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from product.models import *
from blog.models import Tag
from product.forms import ReviewForm
# Create your views here.

def productdetail(request):
    form = ReviewForm()
    if request.method == 'POST' and 'detailed_product' in request.POST:
        form = ReviewForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Review qeyde alindi!')
            return redirect(reverse_lazy('productdetail'))
    context = {
        'form': form
    }
    return render(request,'product-detail.html', context)

def productlist(request):
    category_list = Category.objects.all()
    popular_tags = Tag.objects.annotate(num_tags=models.Count('blog_tags')).order_by('-num_tags')[:5]
    product_list = Product.objects.all()

    context = {
        'categories': category_list,
        'tags': popular_tags,
        'products': product_list
    }
    return render(request,'product-list.html', context)


