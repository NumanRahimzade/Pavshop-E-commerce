from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from core.models import Contact, NewsLatest, Subscription, Tag


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'subject', 'message')
    list_filter = ('full_name', 'email', 'subject')
    search_fields = ('full_name', 'email', 'phone', )


@admin.register(NewsLatest)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at')
    list_filter = ('title', 'created_at')
    search_fields = ('title', 'created_at' )


@admin.register(Subscription)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_at')
    list_filter = ('email', 'created_at')
    search_fields = ('email', )


@admin.register(Tag)
class TagAdmin(TranslationAdmin):
    list_display = ('title','created_at')
    list_filter = ( 'title','created_at')
    search_fields = ('title', )
# admin.site.register([Contact])
