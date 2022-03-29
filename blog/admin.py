from django.contrib import admin

from blog.models import Blog, Tag


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('author', 'title','created_at',)
    list_filter = ( 'author__username','title','created_at')
    search_fields = ('author__username', )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title','created_at')
    list_filter = ( 'title','created_at')
    search_fields = ('title', )

# admin.site.register([Tag, ])
