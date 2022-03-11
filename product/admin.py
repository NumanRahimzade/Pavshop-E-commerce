from django.contrib import admin

from product.models import Category,Product,PropertyName,PropertyValues,ProductVersion,Brand,ProductImages,Discount


admin.site.register([Category,Product,PropertyName,PropertyValues,ProductVersion,Brand,ProductImages,Discount])
