from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from blog.models import Blog, Comment


# admin.site.register(Blog)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','review','created_at')
    list_filter = ('name','created_at')
    search_fields = [ 'name','review']


@admin.register(Blog)
class BlogAdmin(TranslationAdmin):
    list_display = ('author', 'title','created_at',)
    list_filter = ( 'author__username','title','created_at')
    search_fields = ('author__username', )




# admin.site.register([Tag, ])
