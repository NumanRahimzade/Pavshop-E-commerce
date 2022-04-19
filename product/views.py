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
    print(get_category)
    f = ProductVersion.objects.filter(product__category__name__iexact = get_category).exclude(id=id).order_by('-created_at')[:3] 
    
    ###### code above for myself

    form = ReviewForm()
    if request.method == 'POST' and 'detailed_product' in request.POST:
        form = ReviewForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Review qeyde alindi!')
            return redirect(reverse_lazy('productdetail'))
    context = {
        'form': form,
        'pp' : pp,
        'f' : f
    }
    return render(request,'product-detail.html', context)


class PrdoductDetailView(CreateView, DetailView):
    template_name = 'product-detail.html'
    model = ProductVersion
    context_object_name = 'pp'
    form_class = ReviewForm
    success_url = reverse_lazy('')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        get_category = self.object.product.category.name
        f = ProductVersion.objects.filter(product__category__name__iexact = get_category).exclude(id=self.object.id).order_by('-created_at')[:3] 
        context['f'] = f
        return context


    def form_valid(self, form):
        result = super().form_valid(form)
        messages.add_message(self.request, messages.SUCCESS, 'Review qeyde alindi!')
        return result


    ### error ####
    # def form_valid(self, form):
    #     """If the form is valid, save the associated model."""
    #     self.object = form
    #     self.object.productreview = ProductVersion.objects.get(id=self.kwargs['pk'])
    #     # self.object.productreview = ProductVersion.objects.get(id=self.kwargs['pk'])
    #     self.object.save()
    #     print(self.request.POST)
    #     messages.add_message(self.request, messages.SUCCESS, 'Review qeyde alindi!')
    #     return super().form_valid(form)
    
    # def get_success_url(self):
    #     print(self.object.productreview)
    #     return reverse_lazy('productdetail', args=(self.object.productreview.id,))



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


