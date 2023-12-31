# Generated by Django 4.2.6 on 2023-10-13 12:45

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("plans", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Destination",
            fields=[
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("arrival_date", models.DateField()),
                ("lat", models.FloatField()),
                ("long", models.FloatField()),
                ("name", models.TextField()),
                ("place_id", models.TextField()),
                (
                    "plan",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="destinations",
                        to="plans.plan",
                    ),
                ),
            ],
            options={
                "ordering": ["-created"],
                "abstract": False,
            },
        ),
    ]
