from django.contrib import admin
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
# from django.utils.translation import gettext as _


class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'bio', 'image', 'phone', 'address', 'town_city', 'country')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

# admin.site.unregister(BaseUserAdmin)
admin.site.register(User, UserAdmin)
