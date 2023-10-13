from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from weather.serializers import WeatherIO

from api.utils.validate_or_400 import validate_or_400

host_url = "https://api.open-meteo.com/v1/forecast"


class WeatherEndpoint(APIView):
    def post(self, request, format=None):
        # The import is moved here so that we can mock
        # urlopen in the tests.
        from urllib.request import urlopen

        data = validate_or_400(WeatherIO, request.data)
        data = urlopen(
            host_url
            + f"?latitude={data['lat']}&longitude={data['long']}"
            + "&daily=weathercode,temperature_2m_max,temperature_2m_min"
            + "&timezone=GMT"
        ).read()
        return Response({"data": data}, status=status.HTTP_200_OK)
