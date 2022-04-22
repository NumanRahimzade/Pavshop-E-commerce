from unicodedata import category
from django.shortcuts import render
from django.http import HttpResponse
from product.models import Category
from django.db.models import Count
from blog.forms import BlogCommentForm
from core.models import Tag
from .models import *
# from product.models import Product
from django.shortcuts import get_object_or_404


def blog_list(request):
    blogs=Blog.objects.all()
    newblogs=Blog.objects.all().order_by('-created_at')[:3]
    comment=Comment.objects.all()
    categories=Category.objects.all()
    tags=Tag.objects.all()
    tags=Tag.objects.annotate(chapters_cnt=Count('blog_tags')).order_by('-chapters_cnt')
    # comments = Blog.objects.get(id=blog_id).contest_votes.count()
    context={
        'blogs': blogs,
        'comment': comment,
        'categories':categories,
        'newblogs':newblogs,
        'tags':tags

    }
    return render(request, 'blog-list.html',context)


def blog_detail(request, id):
    detailed = get_object_or_404(Blog, id=id)
    blogDetail = Blog.objects.all().exclude(id=id).order_by('-created_at')[:3] #recent post
    # popular_tags = Tag.objects.annotate(num_tags=models.Count('blog_tags')).order_by('-num_tags')[:5] ####comes from templatetags
    # categoryList = Category.objects.all()   ####comes from templatetags
    blogTag = Blog.objects.filter(id=id).first().tags.all()
    mainBlog = Blog.objects.filter(id=id).first()   #main blog
    get_category = mainBlog.category.name
    f = Blog.objects.filter(category__name__iexact = get_category).exclude(id=id).order_by('-created_at')[:3]   #you may like
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
