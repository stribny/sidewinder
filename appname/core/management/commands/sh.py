from django.core import management
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Shortcut for shell_plus"

    def handle(self, *args, **options):
        management.call_command("shell_plus")
