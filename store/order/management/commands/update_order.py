from django.core.management.base import BaseCommand
from order.models import Order
from user.models import User
from product.models import Product

class Command(BaseCommand):
    help = "Update an order"

    def add_arguments(self, parser):
        parser.add_argument('order_id', type=int, help='ID of the order to update')
        parser.add_argument('user_id', type=int, help='ID of the new user')
        parser.add_argument('product_ids', type=int, nargs='+', help='IDs of the products to add to the order')

    def handle(self, *args, **kwargs):
        total_amount = 0
        order_id = kwargs['order_id']
        user_id = kwargs['user_id']
        product_ids = kwargs['product_ids']

        try:
            order = Order.objects.get(pk=order_id)
        except Order.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Order with ID {order_id} does not exist'))
            return
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'User with ID {user_id} does not exist'))
            return

        order.user = user

        order.products.clear()
        for product_id in product_ids:
            try:
                product = Product.objects.get(pk=product_id)
                order.products.add(product)
                total_amount += product.price
            except Product.DoesNotExist:
                self.stdout.write(self.style.ERROR(f'Product with ID {product_id} does not exist'))
                return
        order.total_amount = total_amount
        order.save()

        self.stdout.write(self.style.SUCCESS(f'Updated order: {order}'))