from django.contrib import admin

from contacts import models


class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'created', 'created_ip_address', 'message')
    search_fields = ('email', 'message')
    ordering = ('-created', )
    readonly_fields = ('created', 'created_ip_address',)

    fieldsets = (
        (None, {
            'fields': (
                'email',
                'created',
                'created_ip_address',
                'message')
        }),
    )

    def has_add_permission(self, request, obj=None):
        return False


admin.site.register(models.Contact, ContactAdmin)
