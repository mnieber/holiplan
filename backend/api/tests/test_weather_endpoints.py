import json

import pytest
from django.test import Client

weather_response = {
    "latitude": 52.52,
    "longitude": 13.419998,
    "generationtime_ms": 0.14197826385498047,
    "utc_offset_seconds": 0,
    "timezone": "GMT",
    "timezone_abbreviation": "GMT",
    "elevation": 38.0,
    "daily_units": {
        "time": "iso8601",
        "weathercode": "wmo code",
        "temperature_2m_max": "°C",
        "temperature_2m_min": "°C",
    },
    "daily": {
        "time": [
            "2023-10-14",
            "2023-10-15",
            "2023-10-16",
            "2023-10-17",
            "2023-10-18",
            "2023-10-19",
            "2023-10-20",
        ],
        "weathercode": [80, 3, 3, 3, 3, 61, 80],
        "temperature_2m_max": [19.3, 10.4, 11.3, 12.4, 12.8, 8.1, 4.9],
        "temperature_2m_min": [9.5, 5.9, 5.0, 6.9, 5.8, 2.0, 2.2],
    },
}


class TestWeatherEndpoints:
    @pytest.fixture()
    def client(self):
        return Client()

    @pytest.fixture()
    def urlopen(self, mocker):
        mock = mocker.patch("urllib.request.urlopen")
        mock.return_value.read.return_value = json.dumps(weather_response)
        return mock

    def test_get_weather(self, client: Client, urlopen):
        response = client.post(
            f"/api/weather",
            dict(
                lat="52.52",
                long="13.41",
            ),
            content_type="application/json",
        )

        assert response.status_code == 200
        assert urlopen.called
        args, kwargs = urlopen.call_args
        assert args == (
            "https://api.open-meteo.com/v1/forecast?latitude=52.520000&longitude=13.410000&daily=weathercode,temperature_2m_max,temperature_2m_min&timezone=GMT",
        )
        assert kwargs == {}
