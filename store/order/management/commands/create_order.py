from django.core.management.base import BaseCommand
from order.models import Order
from user.models import User
from product.models import Product
from django.utils import timezone


class Command(BaseCommand):
    help = "Create a new order"

    def handle(self, *args, **kwargs):
        user = User.objects.order_by('?').first()
        products = Product.objects.order_by('?')[:3]
        total_amount = sum(product.price for product in products)
        order_date = timezone.now().date()
        order = Order(
            user=user,
            total_amount=total_amount,
            order_date=order_date,
        )
        order.save()
        order.products.set(products)
        self.stdout.write(self.style.SUCCESS(f'Created order: {order}'))