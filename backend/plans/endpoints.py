from django.shortcuts import get_object_or_404
from plans.models import Plan
from plans.serializers import PlanIO
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.utils.validate_or_400 import validate_or_400


class PlansEndpoint(APIView):
    def post(self, request, format=None):
        data = validate_or_400(PlanIO, request.data)
        plan = Plan(**data)
        plan.save()

        return Response({"data": PlanIO.to_json(plan)}, status=status.HTTP_201_CREATED)


class PlanEndpoint(APIView):
    def get(self, request, plan_id, format=None):
        plan = get_object_or_404(Plan, id=plan_id)
        return Response({"data": PlanIO.to_json(plan)}, status=status.HTTP_200_OK)
