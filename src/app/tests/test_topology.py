import json, pytest, pdb, requests
from uuid import uuid4
# from .mocks.sdn_controllers import get_tsn_topology_info, get_metro_topology_info

topology = {"network_id": "string","network_types": {},"node": [{"node_id": "string","termination_point": {},"l2_node_attributes": {},"l3_node_attributes": {}}],"link": [{"link_id": "string","source": {},"destination": {},"l2_link_attributes": {},"l3_link_attributes": {}}],"l2_topology_attributes": {},"l3_topology_attributes": {}}


def test_get_topologies(test_app):
    response = test_app.delete("/topologies")
    response = test_app.get("/topologies")
    assert response.status_code == 200
    assert response.json() == []

def test_post_topology(test_app):
    response = test_app.post("/topologies", content=json.dumps(topology))
    assert response.status_code == 200
    
# Continue here developing test for each endpoint for topology managing