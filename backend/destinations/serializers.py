from destinations.models import Destination
from rest_framework.serializers import ModelSerializer

from api.model_io import ModelIO


class DestinationSerializer(ModelSerializer):
    class Meta:
        model = Destination
        fields = ["id", "plan", "arrival_date", "lat", "long", "name", "place_id"]


class DestinationIO(ModelIO):
    @classmethod
    def to_json(cls, plan):
        return DestinationSerializer(plan).data

    @classmethod
    def validate(cls, data):
        serializer = DestinationSerializer(data=data)
        if serializer.is_valid():
            return serializer.validated_data, None
        return None, serializer.errors
