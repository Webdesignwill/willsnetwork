from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _

from accounts import admin_forms, models


class UserAdmin(DjangoUserAdmin):
    ordering = ('username',)
    form = admin_forms.UserChangeForm
    add_form = admin_forms.UserCreationForm
    readonly_fields = DjangoUserAdmin.readonly_fields + ('date_joined', )

    filter_horizontal = ()
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined', )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2')
        }),
    )


admin.site.register(models.User, UserAdmin)
