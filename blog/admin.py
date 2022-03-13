from django.contrib import admin

from blog.models import Blog, Tag


admin.site.register([Blog, Tag])
