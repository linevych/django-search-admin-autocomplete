from django.db import models


class DummyModel(models.Model):
    name = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )
    description = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    def __str__(self):
        return str(self.name)
