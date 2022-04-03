from unicodedata import category
from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Blog, Comment,Tag
from product.models import Category
from django.db.models import Count
from blog.forms import BlogCommentForm


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


def blog_detail(request):
    form=BlogCommentForm()
    if request.method=='POST':  
        print('post')
        form=BlogCommentForm(data=request.POST)
        if form.is_valid():
            print('valid')
            form.save()
            print('save')
            print('form is valid')
        # else:
        #     print('form is not valid')
        
    context={
        'form':form
    }
    return render(request, 'blog-detail.html',context)
