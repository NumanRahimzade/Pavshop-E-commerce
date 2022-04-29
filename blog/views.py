from json.tool import main
from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse
from django.views.generic import CreateView, DetailView
from product.models import Category
from django.db.models import Count
from django.urls import reverse_lazy
from django.contrib import messages
from blog.forms import BlogCommentForm
from core.models import Tag
from .models import *
from product.models import Category
# from product.models import Product
from django.shortcuts import get_object_or_404


# def blog_list(request):
#     blogs=Blog.objects.all()
#     newblogs=Blog.objects.all().order_by('-created_at')[:3]
#     comment=Comment.objects.all()
#     categories=Category.objects.all()
#     tags=Tag.objects.all()
#     tags=Tag.objects.annotate(chapters_cnt=Count('blog_tags')).order_by('-chapters_cnt')
#     # comments = Blog.objects.get(id=blog_id).contest_votes.count()
#     context={
#         'blogs': blogs,
#         'comment': comment,
#         'categories':categories,
#         'newblogs':newblogs,
#         'tags':tags

#     }
#     return render(request, 'blog-list.html',context)


class BlogListView(ListView):
    model = Blog
    template_name = 'blog-list.html'
    ordering = ('-created_at', )
    paginate_by = 2
    


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        newblogs=Blog.objects.all().order_by('-created_at')[:3]
        comment=Comment.objects.all() 
        context['newblogs'] = newblogs
        context['comment'] = comment
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.request.GET.get('category_id') # 1
        tag_id = self.request.GET.get('tag_id') # 1
        
        if category_id:
            queryset = queryset.filter(category__id=category_id)
        
        return queryset


def blog_detail(request, id):
    form=BlogCommentForm()
    if request.method=='POST':  
        form=BlogCommentForm(data=request.POST)
        if form.is_valid():
            form.save()
            print('form is valid')
        # else:
        #     print('form is not valid'

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
        'form':form,
        'blog': detailed,
        'bt': blogTag,
        'blg': blogDetail,  
        'mainblog': mainBlog,
        'like': f
    }
    return render(request,'blog-detail.html', context)



class BlogDetailView(CreateView, DetailView):
    template_name = 'blog-detail.html'
    model = Blog
    context_object_name = 'blogs'
    form_class = BlogCommentForm

    # success_url = reverse_lazy('')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories']= Category.objects.all()
        mainBlog = Blog.objects.filter(id=self.object.id).first()  
        get_category = mainBlog.category.name
        context['like']=Blog.objects.filter(category__name__iexact = get_category).exclude(id=self.object.id).order_by('-created_at')[:3]  
        context['tags']=Tag.objects.annotate(chapters_cnt=Count('blog_tags')).order_by('-chapters_cnt')
        context['recentpost']=Blog.objects.all().exclude(id=self.object.id).order_by('-created_at')[:3] 
        context['created']=Blog.objects.all().order_by('-created_at')[:5] 
        context['comments']=Comment.objects.filter(blog=Blog.objects.get(pk=self.object.id))
        context['mainBlog']=mainBlog 
        return context

    def get_queryset(self):
        queryset=super().get_queryset()
        blog_id=self.request.GET.get('blog_id')
        category_id = self.request.GET.get('category_id') # 1
        tag_id=self.request.GET.get('tag_id')
        if blog_id:
            queryset=queryset.filter(blog__id=blog_id)
        if tag_id:
            queryset=queryset.filter(tags__id=tag_id)
        if category_id:
             queryset = queryset.filter(category__id=category_id)
        return queryset
                
      
      


    def form_valid(self, form):

        form.instance.user=self.request.user
        form.instance.blog=self.get_object()
        # form.instance.name=self.request.POST.get('name')
        # form.instance.email=self.request.POST.get('email')
        form.instance.subject=self.request.POST.get('subject')
        form.instance.review=self.request.POST.get('review')
        form.instance.blog=Blog.objects.get(id=self.kwargs['pk'])

        return super().form_valid(form)

     



    def get_success_url(self):
        blogid=self.kwargs['pk']
        return reverse_lazy('blog_detail', kwargs={'pk': blogid})