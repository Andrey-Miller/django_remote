import csv
from django.contrib import admin
from django.http import HttpResponse
from django.db import models

from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['display_id', 'user', 'total_amount', 'order_date']
    list_filter = ['user', 'order_date', 'products']
    search_fields = ['user__name']
    search_help_text = 'Поиск заказа по клиенту'
    readonly_fields = ['order_date']
    fieldsets = [
        ('Основная информация', {
            'fields': ['user', 'total_amount', 'order_date']
        }),
        ('Товары', {
            'fields': ('products',)
        })
    ]
    filter_horizontal = ('products',)

    def save_model(self, request, obj, form, change):
        if not obj.total_amount:
            obj.total_amount = obj.products.aggregate(total=models.Sum('price'))['total']
        super().save_model(request, obj, form, change)
        obj.products.set(form.cleaned_data['products'])
        obj.save()

    def display_id(self, obj):
        return f"Заказ №{obj.id}"
    display_id.short_description = 'Номер заказа'

