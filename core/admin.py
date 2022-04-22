from django.contrib import admin

from core.models import Contact,Tag


admin.site.register([Contact,Tag])
