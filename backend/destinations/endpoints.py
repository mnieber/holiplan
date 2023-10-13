from destinations.models import Destination
from destinations.serializers import DestinationIO
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.utils.validate_or_400 import validate_or_400


class DestinationsEndpoint(APIView):
    def post(self, request, plan_id, format=None):
        data = validate_or_400(DestinationIO, {**request.data, "plan": plan_id})
        destination = Destination(**data)
        destination.save()

        return Response(
            {"data": DestinationIO.to_json(destination)}, status=status.HTTP_201_CREATED
        )
