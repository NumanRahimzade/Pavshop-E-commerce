from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView
from django.urls import reverse_lazy
from django.contrib import messages
from product.models import *
from blog.models import Tag
from product.forms import ReviewForm
# Create your views here.

def productdetail(request, id):

    ###for myself ----- product and you may like   ####  ---- to run code below i have to add 'id' near request and <int:id> in urls #####
    pp = ProductVersion.objects.filter(id=id).first()
    get_category = pp.product.category.name
    f = ProductVersion.objects.filter(product__category__name__iexact = get_category).exclude(id=id).order_by('-created_at')[:3] 
    review_list = pp.reviews.all().order_by('-created_at')
    ###### code above for myself

    form = ReviewForm()
    if request.method == 'POST' and 'detailed_product' in request.POST:
        form = ReviewForm(data=request.POST)
        if form.is_valid():
            
            a = form.save()
            a.productreview = pp
            a.save()

            ############ may be second version of override
            # review = ProductReview(
            #     full_name=request.POST['full_name'],
            #     email=request.POST['email'],
            #     review=request.POST['review'],
            # )
            # review.productreview = pp
            # review.save()
            ############

            messages.add_message(request, messages.SUCCESS, 'Review qeyde alindi!')
            return redirect(reverse_lazy('productdetail', kwargs={'id': pp.id}))
    context = {
        'form': form,
        'pp' : pp,
        'f' : f,
        'review_list': review_list
    }
    return render(request,'product-detail.html', context)


class ProductDetailView(CreateView, DetailView):
    template_name = 'product-detail.html'
    model = ProductVersion
    context_object_name = 'pp'
    form_class = ReviewForm
    # success_url = reverse_lazy('')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        get_category = self.object.product.category.name
        f = ProductVersion.objects.filter(product__category__name__iexact = get_category).exclude(id=self.object.id).order_by('-created_at')[:3] 
        context['f'] = f
        reviews = self.object.reviews.all().order_by('-created_at')
        context['review_list'] = reviews
        return context


    def form_valid(self, form):
        ##### test
        # result = form.save()
        # result.productreview = self.object
        # result.save()
        #####

        ProductReview.objects.create(
                full_name=self.request.POST['full_name'],
                email=self.request.POST['email'],
                review=self.request.POST['review'],
                productreview=ProductVersion.objects.get(id=self.kwargs['pk'])
            )
        messages.add_message(self.request, messages.SUCCESS, 'Review qeyde alindi!')
        return redirect('productdetail')
        # return self.get_success_url()

    
    # def get_success_url(self):
    #       # if you are passing 'pk' from 'urls' to 'DeleteView' for company
    #       # capture that 'pk' as companyid and pass it to 'reverse_lazy()' function
    #     productversionid=self.kwargs['pk']
    #     return reverse_lazy('productdetail', kwargs={'pk': productversionid})



def productlist(request):
    # category_list = Category.objects.all()
    # popular_tags = Tag.objects.annotate(num_tags=models.Count('blog_tags')).order_by('-num_tags')[:5]
    product_list = Product.objects.all()

    context = {
        # 'categories': category_list,
        # 'tags': popular_tags,
        'products': product_list
    }
    return render(request,'product-list.html', context)


