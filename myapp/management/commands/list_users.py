from django.core.management.base import BaseCommand
from myapp.models import CustomUser

class Command(BaseCommand):
    help = 'Lists all users in the database'

    def handle(self, *args, **options):
        users = CustomUser.objects.all()
        if users:
            self.stdout.write(self.style.SUCCESS('Existing users:'))
            for user in users:
                self.stdout.write(f'- {user.username} ({user.email})')
        else:
            self.stdout.write(self.style.WARNING('No users found in the database.')) 