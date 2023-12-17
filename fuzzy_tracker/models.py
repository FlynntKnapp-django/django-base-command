from django.db import models


class Kitten(models.Model):
    """
    Model for `Kitten` objects.
    """

    name = models.CharField(max_length=255, help_text="Name of the kitten")
    age = models.IntegerField(help_text="Age of the kitten")

    def __str__(self):
        return f"{self.name} ({self.age})"
