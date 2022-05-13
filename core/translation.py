from modeltranslation.translator import translator, TranslationOptions
from core.models import Tag

class TagTranslationOption(TranslationOptions):
    fields = ('title', )


translator.register(Tag, TagTranslationOption) 