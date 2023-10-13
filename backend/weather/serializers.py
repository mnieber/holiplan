import rest_framework.serializers as serializers
from rest_framework.serializers import Serializer

from api.model_io import ModelIO


class WeatherSerializer(Serializer):
    lat = serializers.DecimalField(max_digits=9, decimal_places=6)
    long = serializers.DecimalField(max_digits=9, decimal_places=6)


class WeatherIO(ModelIO):
    @classmethod
    def validate(cls, data):
        serializer = WeatherSerializer(data=data)
        if serializer.is_valid():
            return serializer.validated_data, None
        return None, serializer.errors
