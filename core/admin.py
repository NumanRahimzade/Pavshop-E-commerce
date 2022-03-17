from django.contrib import admin

from core.models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'subject', 'message')
    list_filter = ('full_name', 'email', 'subject')
    search_fields = ('full_name', 'email', 'phone', )

# admin.site.register([Contact])
