from modeltranslation.translator import translator, TranslationOptions
from product.models import ProductVersion,Category

class ProductVersionTranslationOption(TranslationOptions):
    fields = ('title','slug')

class CategoryTranslationOption(TranslationOptions):
    fields = ('name',)


translator.register(ProductVersion, ProductVersionTranslationOption) 
translator.register(Category,CategoryTranslationOption)