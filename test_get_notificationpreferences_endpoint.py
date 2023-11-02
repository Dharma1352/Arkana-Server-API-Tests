import requests
import pytest
import jsonschema
from jsonschema import validate

def test_notificationpreferences_endpoint(base_url_frontend, headers):
    # API GET call to finding endpoint
    notificationpreferences_response = requests.get(f"{base_url_frontend}/notifications/settings/{{id}}", headers=headers)
    assert notificationpreferences_response.status_code == 200, (
        f"Status code returned was {notificationpreferences_response.status_code}"
        f"and not a 200 as expected"
    )
    response_body = notificationpreferences_response.json()
#Notification Preferences needs to be NULL data. Verification of NULL validators