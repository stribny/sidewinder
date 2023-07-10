from django.core import management
from django.core.management.base import BaseCommand

from appname.core.models import User


class Command(BaseCommand):
    help = "(Re)creates a fresh development database"

    def handle(self, *args, **options):
        management.call_command("reset_db", "--noinput")
        management.call_command("migrate")

        superuser = User.objects.create(
            username="superuser",
            email="superuser@example.com",
            is_superuser=True,
            is_staff=True,
        )
        superuser.set_password("superuser")
        superuser.save()

        self.stdout.write(self.style.SUCCESS("Fresh environment is ready!"))
