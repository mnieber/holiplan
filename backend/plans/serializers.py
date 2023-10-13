from destinations.serializers import DestinationIO
from plans.models import Plan
from rest_framework.serializers import ModelSerializer

from api.model_io import ModelIO


class PlanSerializer(ModelSerializer):
    class Meta:
        model = Plan
        fields = ["id", "name"]


class PlanIO(ModelIO):
    @classmethod
    def to_json(cls, plan):
        return {
            **PlanSerializer(plan).data,
            "destinations": [
                DestinationIO.to_json(destination)
                for destination in plan.destinations.all()
            ],
        }

    @classmethod
    def validate(cls, data):
        serializer = PlanSerializer(data=data)
        if serializer.is_valid():
            return serializer.validated_data, None
        return None, serializer.errors
