from django.core.management.base import BaseCommand
from faker import Faker

from fuzzy_tracker.models import Kitten

fake = Faker()


class Command(BaseCommand):
    help = "Creates Random Kittens"

    def add_arguments(self, parser):
        parser.add_argument(
            "count", type=int, help="Indicates the number of kittens to be created"
        )

    def handle(self, *args, **kwargs):
        count = kwargs["count"]
        self.stdout.write(f"Creating {count} Random Kittens...")
        for _ in range(count):
            new_name = fake.name()
            self.stdout.write(f"Creating {new_name}...")
            Kitten.objects.create(
                name=new_name, age=fake.pyint(min_value=0, max_value=20)
            )
        self.stdout.write(self.style.SUCCESS(f"Created {count} Random Kittens!"))
