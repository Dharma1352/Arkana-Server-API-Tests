import requests
import pytest
import jsonschema
from jsonschema import validate

def test_findings_endpoint(base_url_frontend, headers):
    # API GET call to finding endpoint
    accId = '433665'
    findings_response = requests.get(f"{base_url_frontend}/findings/rawdata/{accId}?transformData=true", headers=headers)
    assert findings_response.status_code == 200, (
        f"Status code returned was {findings_response.status_code}"
        f"and not a 200 as expected"
    )
    response_body = findings_response.json()
#Need to validate the written response , Not getting the actual response along with data.