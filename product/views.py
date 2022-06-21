from unittest import result
from django.template.defaulttags import register
from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView, ListView
from django.urls import reverse_lazy
from django.contrib import messages
from product.models import *
from core.models import Tag
from product.forms import ReviewForm
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
    paginate_by = 2

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['last']=ProductVersion.objects.last()
        context['categories']= Category.objects.all()    #Category.objects.filter(products__isnull=False).distinct()
        context['colors']=PropertyValues.objects.all()
        context['tags']=Tag.objects.annotate(chapters_cnt=Count('product_tags')).order_by('-chapters_cnt')
        context['brands']=Brand.objects.all()
        context['prices']=ProductVersion.objects.all().order_by('-price')
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


# def productdetail(request, id):

    ###for myself ----- product and you may like   ####  ---- to run code below i have to add 'id' near request and <int:id> in urls #####
    # pp = ProductVersion.objects.filter(id=id).first()
    # get_category = pp.product.category.name
    # f = ProductVersion.objects.filter(product__category__name__iexact = get_category).exclude(id=id).order_by('-created_at')[:3] 
    # review_list = pp.reviews.all().order_by('-created_at')
    # ###### code above for myself

    # form = ReviewForm()
    # if request.method == 'POST' and 'detailed_product' in request.POST:
    #     form = ReviewForm(data=request.POST)
    #     if form.is_valid():
            
    #         a = form.save()
    #         a.productreview = pp
    #         a.save()

            ############ may be second version of override
            # review = ProductReview(
            #     full_name=request.POST['full_name'],
            #     email=request.POST['email'],
            #     review=request.POST['review'],
            # )
            # review.productreview = pp
            # review.save()
            ############

    #         messages.add_message(request, messages.SUCCESS, 'Review qeyde alindi!')
    #         return redirect(reverse_lazy('productdetail', kwargs={'id': pp.id}))
    # context = {
    #     'form': form,
    #     'pp' : pp,
    #     'f' : f,
    #     'review_list': review_list
    # }
    # return render(request,'product-detail.html', context)


class ProductDetailView(CreateView, DetailView):
    template_name = 'product-detail.html'
    model = ProductVersion
    context_object_name = 'pp'
    form_class = ReviewForm
    # success_url = reverse_lazy('')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        detailed = ProductVersion.objects.filter(slug=self.kwargs['slug']).first() 
        get_category = detailed.product.category.name
        f = ProductVersion.objects.filter(product__category__name__iexact = get_category).exclude(slug=self.kwargs['slug']).order_by('-created_at')[:3] 
        context['f'] = f
        reviews = detailed.reviews.all().order_by('-created_at')
        context['review_list'] = reviews
        context['images'] = ProductImages.objects.all()
        return context


    def form_valid(self, form):
        
        form.instance.user = self.request.user
        form.instance.comment = self.request.POST['comment']
        form.instance.productversion = ProductVersion.objects.get(slug=self.kwargs['slug'])
        
        messages.add_message(self.request, messages.SUCCESS, 'Review qeyde alindi!')
        
        return super().form_valid(form)

    
    def get_success_url(self):
        productversionid=self.kwargs['slug']
        return reverse_lazy('productdetail', kwargs={'slug': productversionid})


    @register.filter
    def get_range(value):
        if value < 6:
            return range(1, value+1)
        return range(1, 6)