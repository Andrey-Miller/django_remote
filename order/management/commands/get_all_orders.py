from django.core.management.base import BaseCommand
from order.models import Order


class Command(BaseCommand):
    help = "Gert all orders"

    def handle(self, *args, **kwargs):
        orders = Order.objects.all()
        for order in orders:
            self.stdout.write(str(order))