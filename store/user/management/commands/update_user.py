from django.core.management.base import BaseCommand
from user.models import User


class Command(BaseCommand):
    help = "Update a user info by id"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')
        parser.add_argument('name', type=str, help='User name')
        parser.add_argument('email', type=str, help='User email')
        parser.add_argument('phone_number', type=str, help='User phone')
        parser.add_argument('address', type=str, help='User address')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        name = kwargs.get('name')
        email = kwargs.get('email')
        phone_number = kwargs.get('phone_number')
        address = kwargs.get('address')
        user = User.objects.filter(pk=pk).first()
        user.name = name
        user.email = email
        user.phone_number = phone_number
        user.address = address
        user.save()
        self.stdout.write(self.style.SUCCESS(f'Updated user: {user}'))