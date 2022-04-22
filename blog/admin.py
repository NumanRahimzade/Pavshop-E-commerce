from django.contrib import admin

from blog.models import Blog, Comment


admin.site.register(Blog)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','review','created_at')
    list_filter = ('name','created_at')
    search_fields = [ 'name','review']
    