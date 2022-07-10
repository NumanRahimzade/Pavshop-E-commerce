from django.shortcuts import render
from django.http import HttpResponse
from django.template import context
# from order.models import BillingDetail
from order.forms import ShippingDetailForm


def checkout(request):
    form=ShippingDetailForm()
    if request.method=='POST':  
        form=ShippingDetailForm(data=request.POST)
        if form.is_valid():
            form.save()
            print('form is valid')
        # else:
        #     print('form is not valid')
        
    context={
        'form':form
    }
    return render(request, 'checkout.html',context)

def shoppingcart(request):
    return render(request, 'shopping-cart.html')