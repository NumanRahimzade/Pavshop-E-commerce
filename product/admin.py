from django.contrib import admin

<<<<<<< HEAD
from product.models import Category,Product,PropertyName,PropertyValues,ProductVersion,Brand,ProductImages,Discount,WishList
=======

from product.models import Category,PropertyName,PropertyValues,ProductVersion,Brand,ProductImages,Discount
>>>>>>> b8a2857d90bf014ac3c4d07faccf7d9fb6f7fcbf


admin.site.register([Category,Product,PropertyName,PropertyValues,ProductVersion,Brand,ProductImages,Discount,WishList])
