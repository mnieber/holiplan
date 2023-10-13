from django.db import models

from app.models import Entity


class Plan(Entity):
    name = models.TextField()

    def __str__(self):
        return f"Plan: {self.id}"
