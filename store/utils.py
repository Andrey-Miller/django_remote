from faker import Faker
from user.models import User
from product.models import Product
from order.models import Order

fake = Faker()


def create_fake_users(num_users):
    for _ in range(num_users):
        user = User(
            name=fake.name(),
            email=fake.email(),
            phone_number=fake.phone_number(),
            address=fake.address(),
            registration_date=fake.date_this_year()
        )
        user.save()


def create_fake_products(num_products):
    for _ in range(num_products):
        product = Product(
            name=fake.word().capitalize(),
            description=fake.text(),
            price=fake.random_number(digits=3),
            quantity=fake.random_number(digits=2),
            added_date=fake.date_this_year()
        )
        product.save()


def create_fake_orders(num_orders):
    for _ in range(num_orders):
        user = User.objects.order_by('?').first()
        products = Product.objects.order_by('?')[:3]
        total_amount = sum(product.price for product in products)
        order_date = fake.date_this_year()

        order = Order.objects.create(
            user=user,
            total_amount=total_amount,
            order_date=order_date
        )
        order.products.set(products)
