import pytest
from destinations.models import Destination
from django.test import Client
from plans.models import Plan


class TestPlanEndpoints:
    @pytest.fixture()
    def client(self):
        return Client()

    @pytest.fixture()
    def plan(self):
        plan = Plan.objects.create(name="Spain")
        return plan

    @pytest.fixture()
    def destination(self, plan: Plan):
        destination = Destination.objects.create(
            plan=plan,
            name="Barcelona",
            arrival_date="2023-01-02",
            lat="123.45",
            long="234.56",
            place_id="abcdef",
        )
        return destination

    @pytest.mark.django_db()
    def test_create_plan(self, client: Client):
        response = client.post(
            "/api/plans", dict(name="Spain"), content_type="application/json"
        )

        assert response.status_code == 201
        response_data = response.json()["data"]
        id = response_data["id"]
        assert id
        assert response_data["name"] == "Spain"
        assert response_data["destinations"] == []

    @pytest.mark.django_db()
    def test_get_plan(self, client: Client, plan: Plan, destination: Destination):
        response = client.get(f"/api/plans/{plan.id}", content_type="application/json")

        assert response.status_code == 200
        response_data = response.json()["data"]
        assert response_data["id"] == str(plan.id)
        assert len(response_data["destinations"]) == 1
        assert response_data["destinations"][0]["id"] == str(destination.id)

    @pytest.mark.django_db()
    def test_add_destination_to_plan(self, client: Client, plan: Plan):
        response = client.post(
            f"/api/plans/{plan.id}/destinations",
            dict(
                name="Barcelona",
                arrival_date="2023-01-02",
                lat="123.45",
                long="234.56",
                place_id="abcdef",
            ),
            content_type="application/json",
        )

        assert response.status_code == 201
        response_data = response.json()["data"]
        assert response_data["name"] == "Barcelona"
