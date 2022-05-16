from dataclasses import field
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from product.models import Category,Product,PropertyName,PropertyValues,ProductVersion,Brand,ProductImages,Discount, Review,WishList



class ProductImageInlineAdmin(admin.TabularInline):
    model = ProductImages



# admin.site.register([WishList])


# from product.models import Category,Product,PropertyName,PropertyValues,ProductVersion,Brand,ProductImages,Discount,WishList, ProductReview
    
@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ('name', 'created_at')
    list_filter = ( 'name','created_at')
    search_fields = ['name']
  

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('brand', 'created_at')
    list_filter = ( 'brand','category','created_at')
    search_fields = ['brand__name', 'category__name']
    search_fields = ('name', )


@admin.register(PropertyName)
class PropertyNameAdmin(admin.ModelAdmin):
    list_display = ('name', 'category','created_at')
    list_filter = ( 'name','category','created_at')
    search_fields = ('name', 'category__name')


@admin.register(PropertyValues)
class PropertyValuesAdmin(admin.ModelAdmin):
    list_display = ('value','propertyname','created_at')
    list_filter = ('value','propertyname','created_at')
    search_fields = ('value', 'propertyname__name')


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name','created_at')
    list_filter = ('name','created_at')
    search_fields = ('name', )


@admin.register(ProductImages)
class ProductImagesAdmin(admin.ModelAdmin):
    list_display = ('version','created_at', 'image', 'cover_image')
    list_filter = ('version','created_at')
    search_fields = ('version__title', )


@admin.register(ProductVersion)
class ProductVersionAdmin(TranslationAdmin):
    list_display = ('title', 'code', 'price', 'stock', 'created_at')
    list_filter = ('product__category__name', 'created_at')
    search_fields = ('title', 'price', 'code')
    inlines = [ProductImageInlineAdmin, ]


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('title','percentage','value','created_at')
    list_filter = ('title','created_at')
    search_fields = ('title', 'percentage','value')


@admin.register(WishList)
class WishListAdmin(admin.ModelAdmin):
    list_display = ('user','created_at')
    list_filter = ('productversion','user','created_at')
    search_fields = ( 'user__username', )



@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user','productversion','comment','created_at')
    list_filter = ('productversion','user','created_at')
    search_fields = [ 'user__username','productversion__title','comment']
    
    


# @admin.register(ProductReview)
# class ProductReview(admin.ModelAdmin):
#     list_display = ('full_name', 'email', 'review','created_at')
#     list_filter = ('full_name', 'email', 'created_at')
#     search_fields = ( 'full_name', 'email',  )
    # list_display = ('user', 'email', 'review','created_at')
    # list_filter = ('user', 'email', 'created_at')
    # search_fields = ( 'user', 'email',  )

# admin.site.register([ProductVersion])
