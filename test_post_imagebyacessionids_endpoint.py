import requests
import pytest
import jsonschema
from jsonschema import validate

ImageAccessionByGroupSchema = {
    "type": "object",
    "properties": {
        "acc_image_id": {"type": "number"},
        "guid": {"type": "string"},
        "acc_id": {"type": "number"},
        "label": {"type": "string"},
        "image_thumbnail": {"type": "string"},
        "data": {"type": "string"}
    },
}
def test_imagebyacessionids_endpoint(base_url_frontend, headers):
    # API GET call to finding endpoint
    imagebyacessionids_response = requests.post(f"{base_url_frontend}/images", headers=headers)
    assert imagebyacessionids_response.status_code == 200, (
        f"Status code returned was {imagebyacessionids_response.status_code}"
        f"and not a 200 as expected"
    )
    response_body = imagebyacessionids_response.json()
    # We are not getting actual response so, we couldn't able to validate the same.

def validateResponse(response):
    try:
        validate(instance=response, schema=ImageAccessionByGroupSchema)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True
