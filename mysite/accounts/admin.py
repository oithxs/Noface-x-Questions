from django.contrib import admin
from django.contrib.auth.models import Group

from .models import User

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

class UserAdmin(BaseUserAdmin):
    list_display = ('account_id', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('account_id', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'birth_date')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        (_('Important dates'), {'fields': ('created_at', 'updated_at')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('account_id', 'email', 'password1', 'password2'),
        }),
    )
    search_fields = ('account_id', 'email', 'first_name', 'last_name')
    ordering = ('account_id',)
    filter_horizontal = ()

# モデルを管理サイトに登録
# admin.site.register(User, UserAdmin)

admin.site.register(User, UserAdmin)  # Userモデルを登録
admin.site.unregister(Group)  # Groupモデルは不要のため非表示にします
