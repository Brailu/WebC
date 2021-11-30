from django.db import models


class Calculator(models.Model):

    name = models.CharField(
        "name",
        max_length=32,
        unique=True
    )

    def __str__(self):
        return self.name
