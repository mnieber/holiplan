from django.contrib import admin

from destinations.admin import DestinationInline
from plans import models


@admin.register(models.Plan)
class PlanAdmin(admin.ModelAdmin):
    inlines = (DestinationInline,)
