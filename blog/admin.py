from django.contrib import admin

from blog.models import Blog, Comment,Tag


admin.site.register([Blog,Tag])


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','review','created_at')
    list_filter = ('name','created_at')
    search_fields = [ 'name','review']
    