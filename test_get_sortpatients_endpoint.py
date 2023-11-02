import requests
import pytest
import jsonschema
from jsonschema import validate

sortpatientsSchema = {
    "type": "object",
    "properties": {
        "message": {"type": "string"}
    },
}
def test_sortpatients_endpoint(base_url_frontend, headers):
    # API GET call to finding endpoint
    groupId = '7653'
    sortOption = '2'
    sortpatients_response = requests.get(f"{base_url_frontend}/patients/sort/{groupId}?sortOption={sortOption}", headers=headers)
    assert sortpatients_response.status_code == 200, (
        f"Status code returned was {sortpatients_response.status_code}"
        f"and not a 200 as expected"
    )
    response_body = sortpatients_response.json()
#We are not getting actual response so, we couldn't able to validate the same.