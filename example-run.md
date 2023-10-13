# POST data is validated

curl -X POST -H "Content-Type: application/json" -d '{"lat": "52.52", "loooong": "13.41"}' localhost:8000/api/weather

{"long":["This field is required."]}

# The weather data can be requested

curl -X POST -H "Content-Type: application/json" -d '{"lat": "52.52", "long": "13.41"}' localhost:8000/api/weather

{"data":"{\"latitude\":52.52,\"longitude\":13.419998,\"generationtime_ms\":0.15807151794433594,\"utc_offset_seconds\":0,\"timezone\":\"GMT\",\"timezone_abbreviation\":\"GMT\",\"elevation\":38.0,\"daily_units\":{\"time\":\"iso8601\",\"weathercode\":\"wmo code\",\"temperature_2m_max\":\"°C\",\"temperature_2m_min\":\"°C\"},\"daily\":{\"time\":[\"2023-10-14\",\"2023-10-15\",\"2023-10-16\",\"2023-10-17\",\"2023-10-18\",\"2023-10-19\",\"2023-10-20\"],\"weathercode\":[80,80,3,3,3,3,61],\"temperature_2m_max\":[19.3,10.6,11.0,12.1,12.6,8.7,7.4],\"temperature_2m_min\":[9.2,6.6,5.0,6.0,5.7,3.1,0.8]}}"}

# A plan can be created

curl -X POST -H "Content-Type: application/json" -d '{"name":"Hi"}' localhost:8000/api/plans

{"data":{"id":"df21fcdf-4787-4bf0-a7f9-2bccf7cfd850","name":"Hi","destinations":[]}}

# Destinations can be added

curl -X POST -H "Content-Type: application/json" -d '{"name":"Hello", "arrival_date": "2023-02-03", "place_id": "ok", "lat": "123.45", "long": "234.56"}' localhost:8000/api/plans/df21fcdf-4787-4bf0-a7f9-2bccf7cfd850/destinations

{"data":{"plan":"df21fcdf-4787-4bf0-a7f9-2bccf7cfd850","arrival_date":"2023-02-03","lat":"123.450000","long":"234.560000","name":"Hello","place_id":"ok"}}

# To add a destination, you need a valid plan

curl -X POST -H "Content-Type: application/json" -d '{"name":"Hello again", "arrival_date": "2023-02-03", "place_id": "ok", "lat": "123.45", "long": "234.56"}' localhost:8000/api/plans/df21fcdf-4787-4bf0-a7f9-2bccf7cf0000/destinations

{"plan":["Invalid pk \"df21fcdf-4787-4bf0-a7f9-2bccf7cf0000\" - object does not exist."]}

# A plan can be fetched

curl -H "Accept: application/json" localhost:8000/api/plans/df21fcdf-4787-4bf0-a7f9-2bccf7cfd850

{"data":{"id":"df21fcdf-4787-4bf0-a7f9-2bccf7cfd850","name":"Hi","destinations":[{"plan":"df21fcdf-4787-4bf0-a7f9-2bccf7cfd850","arrival_date":"2023-02-03","lat":"123.450000","long":"234.560000","name":"Hello","place_id":"ok"}]}}
