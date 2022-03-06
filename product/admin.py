from django.contrib import admin

from product.models import Category,PropertyName,PropertyValues,ProductVersion,Brand,ProductImages,Discount


admin.site.register([Category,PropertyName,PropertyValues,ProductVersion,Brand,ProductImages,Discount])
