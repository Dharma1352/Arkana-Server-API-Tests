import requests
import pytest
import jsonschema
from jsonschema import validate

PhysiciansBynameSchema = {
    "type": "object",
    "properties": {
        "refmd_id": {"type": "number"},
        "guid": {"type": "string"},
        "code": {"type": "string"},
        "first_name": {"type": "string"},
        "mid_name": {"type": "string"},
        "last_name": {"type": "string"},
        "gen_title": {"type": "string"},
        "speciality_id": {"type": "number"},
        "cell_phone": {"type": "string"},
        "active": {"type": "string"}
    }
}

def test_physicianname_endpoint(base_url_frontend, headers):
    # API GET call to finding endpoint
    physicianname_response = requests.get(f"{base_url_frontend}/refmd/current", headers=headers)
    assert physicianname_response.status_code == 200, (
        f"Status code returned was {physicianname_response.status_code}"
        f"and not a 200 as expected"
    )
    response_body = physicianname_response.json()
    isValid = validateResponse(response_body)
    assert isValid, (
        f"Response Validation Failed."
    )
 # We are not getting actual response so, we couldn't able to validate the same.
def validateResponse(response):
    try:
        validate(instance=response, schema=PhysiciansBynameSchema)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True