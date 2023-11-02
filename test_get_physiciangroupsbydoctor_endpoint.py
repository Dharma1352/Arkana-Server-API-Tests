import requests
import jsonschema
from jsonschema import validate

groupForDoctorSchema = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "guid": {"type": "string"},
        "group_id": {"type": "number"},
        "entity_type": {"type": "string"},
        "refmd_id": {"type": "number"},
        "name": {"type": "string"},
        "active": {"type": "string"}
    },
}

def test_physiciangroupsbydoctor_endpoint(base_url_frontend, headers):
    # API GET call to finding endpoint
    physiciangroupsbydoctor_response = requests.get(f"{base_url_frontend}/group/groups/for/doctor", headers=headers)
    assert physiciangroupsbydoctor_response.status_code == 200, (
        f"Status code returned was {physiciangroupsbydoctor_response.status_code}"
        f"and not a 200 as expected"
    )
    response_body = physiciangroupsbydoctor_response.json()
    # Validating the json data
    for response in response_body:
        if response:
            isValid = validateResponse(response)
            assert isValid, (
                f"Response Validation Failed. "
            )
def validateResponse(response):
    try:
        validate(instance=response, schema=groupForDoctorSchema)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True