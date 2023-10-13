from django.db import models

from app.models import Entity


class Destination(Entity):
    class Meta:
        ordering = ["arrival_date"]

    plan = models.ForeignKey(
        "plans.Plan", on_delete=models.CASCADE, related_name="destinations"
    )
    arrival_date = models.DateField()
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    long = models.DecimalField(max_digits=9, decimal_places=6)
    name = models.TextField()
    place_id = models.TextField()

    def __str__(self):
        return f"Destination: {self.name}"
