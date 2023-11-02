import requests
import pytest
import jsonschema
from jsonschema import validate
def test_patientsfor_agroup_endpoint (base_url_frontend, headers):
    # API GET call to finding endpoint
    groupId = '7653'
    sortOption = '1'
    patientsfor_agroup_response = requests.get(f"{base_url_frontend}/patients/sort/{groupId}?sortOption={sortOption}", headers=headers)
    assert patientsfor_agroup_response.status_code == 200, (
        f"Status code returned was {patientsfor_agroup_response.status_code}"
        f"and not a 200 as expected"
    )
    response_body = patientsfor_agroup_response.json()
#We are not getting actual response so, we couldn't able to validate the same.
