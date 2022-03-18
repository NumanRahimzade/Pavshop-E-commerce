from django.contrib import admin

from product.models import Category,Product,PropertyName,PropertyValues,ProductVersion,Brand,ProductImages,Discount, Review,WishList


class ProductVersionInlineAdmin(admin.TabularInline):
    model = ProductVersion

class PropertyValueInlineAdmin(admin.TabularInline):
    model = PropertyValues

class DiscountInlineAdmin(admin.TabularInline):
    model = Discount

class PropertyNameInlineAdmin(admin.TabularInline):
    model = PropertyName

class ProductImageInlineAdmin(admin.TabularInline):
    model = ProductImages

class ProductInlineAdmin(admin.TabularInline):
    model = Product


# admin.site.register([WishList])

@admin.register(ProductVersion)
class ProductVersionAdmin(admin.ModelAdmin):
    inlines = [ProductImageInlineAdmin, ]
    list_display = ('title', 'code', 'price','stock', 'created_at')
    list_filter = ( 'created_at', )
    search_fields = ('title', 'code')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [ProductInlineAdmin, PropertyNameInlineAdmin, ]
    list_display = ('name', 'created_at')
    list_filter = ( 'name','created_at')
    search_fields = ['name']
  

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductVersionInlineAdmin, ]
    list_display = ('brand', 'created_at')
    list_filter = ( 'brand','category','created_at')
    search_fields = ['brand__name', 'category__name']

@admin.register(PropertyName)
class PropertyNameAdmin(admin.ModelAdmin):
    inlines = [PropertyValueInlineAdmin, ]
    list_display = ('name', 'category','created_at')
    list_filter = ( 'name','category','created_at')
    search_fields = ['name', 'category__name']


@admin.register(PropertyValues)
class PropertyValuesAdmin(admin.ModelAdmin):
    list_display = ('value','propertyname','created_at')
    list_filter = ('value','propertyname','created_at')
    search_fields = ['value', 'propertyname__name']


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    inlines = [ProductInlineAdmin, ]
    list_display = ('name','created_at')
    list_filter = ('name','created_at')
    search_fields = ['name', ]

@admin.register(ProductImages)
class ProductImagesAdmin(admin.ModelAdmin):
    list_display = ('version','created_at')
    list_filter = ('version','created_at')
    search_fields = ['version__title', ]


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    inlines = [ProductVersionInlineAdmin, ]
    list_display = ('title','percentage','value','created_at')
    list_filter = ('title','created_at')
    search_fields = ['title', 'percentage','value']


@admin.register(WishList)
class WishListAdmin(admin.ModelAdmin):
    list_display = ('user','created_at')
    list_filter = ('productversion','user','created_at')
    search_fields = [ 'user__username',]



@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user','productversion','comment','created_at')
    list_filter = ('productversion','user','created_at')
    search_fields = [ 'user__username','productversion__title','comment']
    