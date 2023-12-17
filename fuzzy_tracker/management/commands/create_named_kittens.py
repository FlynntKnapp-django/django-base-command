from django.core.management.base import BaseCommand

from fuzzy_tracker.models import Kitten


class Command(BaseCommand):
    help = "Creates Named Kittens"

    def handle(self, *args, **kwargs):
        self.stdout.write(f"Creating Named Kittens...")
        Kitten.objects.create(name="Felix", age=3)
        Kitten.objects.create(name="Garfield", age=5)
        Kitten.objects.create(name="Sylvester", age=4)
        Kitten.objects.create(name="Tom", age=2)
        Kitten.objects.create(name="Greta", age=10)
        Kitten.objects.create(name="Dezzi", age=13)
        Kitten.objects.create(name="Bunbun", age=13)
        self.stdout.write(self.style.SUCCESS(f"Created Named Kittens!"))
