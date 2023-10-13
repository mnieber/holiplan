from destinations.endpoints import DestinationsEndpoint
from django.urls import path
from plans.endpoints import PlanEndpoint, PlansEndpoint
from weather.endpoints import WeatherEndpoint

urlpatterns = [
    path("plans", PlansEndpoint.as_view(), name="plans"),
    path("plans/<str:plan_id>", PlanEndpoint.as_view(), name="plan"),
    path(
        "plans/<str:plan_id>/destinations",
        DestinationsEndpoint.as_view(),
        name="destinations",
    ),
    path("weather", WeatherEndpoint.as_view(), name="weather"),
]
