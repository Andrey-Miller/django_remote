from django.contrib import admin

from .models import User


@admin.register(User)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number', 'address']
    list_filter = ['registration_date']
    readonly_fields = ['registration_date']
    search_fields = ['name', 'phone_number']
    search_help_text = 'Поиск клиента по имени и номеру телефона'
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name']
            }
        ),
        (
            'Контакты',
            {
                'description': 'Контактная информация клиента',
                'fields': ['phone_number', 'email'],
            },
        ),
        (
            'Адрес',
            {
                'classes': ['collapse'],
                'description': 'Адрес для доставки',
                'fields': ['address'],
            }
        ),
    ]
