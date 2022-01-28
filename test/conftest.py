import pytest
import requests
import json

@pytest.fixture
def authToken():
    """client_auth = requests.auth.HTTPBasicAuth('client id',
                                              'client secret')
    #post_data = {"grant_type": "client_credentials"}
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    res = requests.post('url', data = post_data, auth = client_auth, headers = headers)
    a = res.json()"""
    Token="05d74d0e5c158e3677b2f164d7efb3a370476f008989842087883af327afda1f"
    return Token
