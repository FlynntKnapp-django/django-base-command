from django.core.management.base import BaseCommand

from fuzzy_tracker.models import Kitten


class Command(BaseCommand):
    help = "Creates Named Kittens"

    def handle(self, *args, **kwargs):
        self.stdout.write("Creating Named Kittens...")

        # Define a dictionary of kitten names and ages
        kittens = {
            "Felix": 3,
            "Garfield": 5,
            "Sylvester": 4,
            "Tom": 2,
            "Greta": 10,
            "Dezzi": 13,
            "Bunbun": 13,
        }

        # Iterate over the dictionary and create each kitten
        for name, age in kittens.items():
            Kitten.objects.create(name=name, age=age)

        self.stdout.write(self.style.SUCCESS("Created Named Kittens!"))
