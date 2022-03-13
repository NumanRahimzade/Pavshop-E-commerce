from django.contrib import admin

from blog.models import Blog, Tag, CategoryBlog


admin.site.register([Blog, Tag, CategoryBlog])
