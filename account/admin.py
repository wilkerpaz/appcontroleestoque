from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from .forms import UserAdminCreationForm, UserAdminForms

# from .models import User
User = get_user_model()


class UserAdmin(BaseUserAdmin):
    add_forms = UserAdminCreationForm

    form = UserAdminForms
    fieldsets = (
        (None, {'fields': ('username', 'name', 'email')}),
        # (_('Important dates'), {'fields': ('last_login',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
    )

    add_fieldsets = (
        (None, {'fields': ('username', 'name', 'email', 'passwords1', 'passwords2')}),
    )

    list_display = ['username', 'name', 'email', 'is_active', 'is_staff', 'date_joined', 'last_login']
    ordering = ('username',)


admin.site.register(User, UserAdmin)
