from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Prints a string"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS("Cats rule, dogs drool!") + "\n")
