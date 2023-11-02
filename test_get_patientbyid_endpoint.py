import requests
import pytest
import jsonschema
from jsonschema import validate

patientsSchema = {
    "properties": {
        "result":{
            "type": "object",
            "properties": {
                "id": {"type": "number"},
                "guid": {"type": "string"},
                "first_name": {"type": "string"},
                "last_name": {"type": "string"},
                "sex": {"type": "string"},
                "age": {"type": "number"},
                "accessions":{
                    "type":"array",
                    "properties":{
                        "acc_id": {"type": "number"},
                        "accession_no": {"type": "string"}
                    }
                }
            }

        }

    }
}

def test_patientbyid_endpoint(base_url_frontend, headers):
    # API GET call to patient endpoint
    patientbyId = '238803'
    patientbyid_response = requests.get(f"{base_url_frontend}/patients/id/{patientbyId}", headers=headers)
    assert patientbyid_response.status_code == 200, (
        f"Status code returned was {patientbyid_response.status_code} "
        f"and not a 200 as expected"
    )
    response_body = patientbyid_response.json()
    isValid = validateResponse(response_body)
    assert isValid, (
        f"Response Validation Failed. "
    )
    # We are not getting actual response so, we couldn't able to validate the same.

def validateResponse(response):
    try:
        validate(instance=response, schema=patientsSchema)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True