from modeltranslation.translator import translator, TranslationOptions
from .models import Blog

class BlogTranslationOption(TranslationOptions):
    fields = ('title', 'slug', 'description')


translator.register(Blog, BlogTranslationOption)