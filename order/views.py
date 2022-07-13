from itertools import count
from django.shortcuts import render
from django.http import HttpResponse
from django.template import context
# from order.models import BillingDetail
from order.forms import ShippingDetailForm
import stripe
from django.conf import settings
from .models import Basket, BasketItem
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

def checkout(request):
    products = BasketItem.objects.all().exclude(basket__status=True).exclude(count=0)
    a = 0
    for i in products:
        a += i.price
    print(a)
    form=ShippingDetailForm()
    if request.method=='POST':  
        form=ShippingDetailForm(data=request.POST)
        if form.is_valid():
            form.save()
            print('form is valid')
        # else:
        #     print('form is not valid')

        ######payment STRIPE
            
            # basket_product = BasketItem.objects.filter(
            #         user=request.user, basket__status=False).all()
            # listadd = []
            # for i in basket_product:
            #     listadd.append(i.price, i.count)
            
            # domain = 'http://127.0.0.1:8000/en/checkout'
            # line_items = []
            # stripe.api_key = settings.STRIPE_SECRET_KEY
            # checkout_session = stripe.checkout.Session.create(
            #     line_items=line_items,
            #     payment_method_types=[
            #         {
            #         # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
            #         'price': '3',
            #         'quantity': 1,
            #         },
            #     ],
            #     mode='payment',
            #     success_url=domain + '/success/',
            #     cancel_url=domain + '/checkout/',
            # )
            # Basket.objects.filter(status=False).filter(user=request.user).update(
            #     status=True)
        ###### STRIPE
    context={
        'form':form,
        'total':a,
        'products': products,
    }
    return render(request, 'checkout.html',context)

def shoppingcart(request):
    return render(request, 'shopping-cart.html')


# def payment(request):

#     products = BasketItem.objects.all().exclude(basket__status=True).exclude(count=0)
#     a = 0
#     for i in products:
#         a += i.price
#     print(a)
#     context={
#         'total':a,
#         'products': products,

#     }
#     return render(request, 'payment.html', context=context)