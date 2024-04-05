import json, pytest, pdb
from uuid import uuid4

request_data = {"name": "default_name", "description": "default_description", "url": "https://localhost", "port": 0, "username": "default_username", "password": "default_password", "type": "type_not_defined"}    


def test_get_controllers(test_app):
    response = test_app.get("/controllers")
    assert response.status_code == 200
    # assert response.json() == []

def test_post_controllers(test_app):
    response = test_app.post("/controllers", content=json.dumps(request_data))
    assert response.status_code == 200

# Continue here developing test for each endpoint for controllers managing