import requests
import pytest
import jsonschema
from jsonschema import validate

def test_notification_endpoint(base_url_frontend, headers):
    # API GET call to finding endpoint
    notification_response = requests.get(f"{base_url_frontend}/notifications", headers=headers)
    assert notification_response.status_code == 200, (
        f"Status code returned was {notification_response.status_code}"
        f"and not a 200 as expected"
    )
    response_body = notification_response.json()

#We are not getting actual response so, we couldn't able to validate the same.