from decimal import Decimal
from django.core.management.base import BaseCommand
from product.models import Product
from django.utils.crypto import get_random_string
from django.utils import timezone


class Command(BaseCommand):
    help = "Create a new product"

    def handle(self, *args, **kwargs):
        name = get_random_string(length=10,
                                 allowed_chars='abcdefghijklmnopqrstuvwxyz').capitalize()
        description = get_random_string(15)
        price = Decimal(get_random_string(length=2, allowed_chars='0123456789')).quantize(Decimal('.01'))
        quantity = int(get_random_string(length=3, allowed_chars='123456789'))
        added_date = timezone.now().date()
        product = Product(
            name=name,
            description=description,
            price=price,
            quantity=quantity,
            added_date=added_date,
        )
        product.save()
        self.stdout.write(self.style.SUCCESS(f'Created product: {product}'))


