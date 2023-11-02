import requests
import pytest
import requests
import pytest
import jsonschema
from jsonschema import validate


PhysiciansByGroupSchema = {
    "type": "object",
    "properties": {
        "refmd_id": {"type": "number"},
        "guid": {"type": "string"},
        "code": {"type": "string"},
        "first_name": {"type": "string"},
        "last_name": {"type": "string"},
        "gen_title": {"type": "string"},
        "speciality_id": {"type": "number"},
        "email": {"type": "null"},
        "cell_phone": {"type": "string"},
        "active": {"type": "string"},
    },
}
def test_pysiciansforgroups_endpoint(base_url_frontend, headers):
    # API GET call to finding endpoint
    groupId = '15619'
    pysicianforgroup_response = requests.get(f"{base_url_frontend}/group/?group_id={groupId}", headers=headers)
    assert pysicianforgroup_response.status_code == 200, (
        f"Status code returned was {pysicianforgroup_response.status_code}"
        f"and not a 200 as expected"
    )
    response_body = pysicianforgroup_response.json()
    # Validating the json data
    for response in response_body:
        if response:
            isValid = validateResponse(response)
            assert isValid, (
                f"Response Validation Failed. "
            )
def validateResponse(response):
    try:
        validate(instance=response, schema=PhysiciansByGroupSchema)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True