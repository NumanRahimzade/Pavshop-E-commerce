from django.contrib import admin

from blog.models import Blog, Comment,Tag


admin.site.register([Blog,Tag])


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user','blog','review','created_at')
    list_filter = ('blog','user','created_at')
    search_fields = [ 'user__username','blog__title','review']
    