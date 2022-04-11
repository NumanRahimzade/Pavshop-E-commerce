from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from product.models import Product
from django.shortcuts import get_object_or_404


def blog_list(request):
    return render(request, 'blog-list.html')


def blog_detail(request, id):
    detailed = get_object_or_404(Blog, id=id)
    blogDetail = Blog.objects.all()
    # popular_tags = Tag.objects.annotate(num_tags=models.Count('blog_tags')).order_by('-num_tags')[:5]
    # categoryList = Category.objects.all()
    blogTag = Blog.objects.filter(id=id).first().tags.all()
    mainBlog = Blog.objects.filter(id=id).first()
    get_category = mainBlog.category.name
    f = Blog.objects.filter(category__name__iexact = get_category).exclude(id=id).order_by('-created_at')[:3]   #eger blog producta yazilarsa bu
    # f = Product.objects.filter(category__name__iexact = get_category).order_by('-created_at')[:3]

    
    # youMayLike = Product.objects.filter(category__name = 'wear)')

    context = {
        # 'categories': categoryList,
        # 'tags': popular_tags,
        'blog': detailed,
        'bt': blogTag,
        'blg': blogDetail,
        'mainblog': mainBlog,
        'like': f
    }
    return render(request,'blog-detail.html', context)
