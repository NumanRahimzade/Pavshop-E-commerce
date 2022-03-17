from django.contrib import admin

from product.models import Category,Product,PropertyName,PropertyValues,ProductVersion,Brand,ProductImages,Discount,WishList


class ProductVersionInlineAdmin(admin.TabularInline):
    model = ProductVersion

    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('brand', 'created_at')
    list_filter = ('brand__name', 'created_at')
    search_fields = ('brand__name', )
    inlines = [ProductVersionInlineAdmin, ]
    

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    list_filter = ( 'name','created_at')
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


class ProductImagesInlineAdmin(admin.TabularInline):
    model = ProductImages


@admin.register(ProductVersion)
class ProductVersionAdmin(admin.ModelAdmin):
    list_display = ('title', 'code', 'price', 'stock', 'created_at')
    list_filter = ('product__category__name', 'created_at')
    search_fields = ('title', 'price', 'code')
    inlines = [ProductImagesInlineAdmin, ]
    # fieldsets = [
    #     ('Standard info', {
    #         'fields': ('title', 'created_at'),
    #         'classes': ('wide',)
    #     }),
    #     ('Other', {
    #         'fields': ('price', 'code', 'stock' )
    #     }),
    # ]

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

# admin.site.register([ProductVersion])
