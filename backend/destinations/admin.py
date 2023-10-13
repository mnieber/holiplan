from django.contrib import admin

from destinations import models


class DestinationInline(admin.TabularInline):
    model = models.Destination
    extra = 3


@admin.register(models.Destination)
class DestinationAdmin(admin.ModelAdmin):
    pass
