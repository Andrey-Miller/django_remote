from django.core.management.base import BaseCommand
from user.models import User


class Command(BaseCommand):
    help = "Delete a user"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        user = User.objects.filter(pk=pk).first()
        if user is not None:
            user.delete()
        self.stdout.write(self.style.SUCCESS(f'Successfully deleted user: {user}'))